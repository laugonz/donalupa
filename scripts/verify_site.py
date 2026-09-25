#!/usr/bin/env python3
"""Static integrity checks for the hand-written Doña Lupa website."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parent.parent
PRODUCT_PAGES = {
    ROOT / "index.html",
    ROOT / "es" / "index.html",
    ROOT / "it" / "index.html",
    ROOT / "pt" / "index.html",
    ROOT / "fr" / "index.html",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1_count = 0
        self.canonical_count = 0
        self.links: list[str] = []
        self.alternates: list[tuple[str, str]] = []
        self.json_ld: list[str] = []
        self.summaries: list[str] = []
        self._json_parts: list[str] | None = None
        self._summary_parts: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical_count += 1
        if tag == "link" and values.get("rel") == "alternate" and values.get("hreflang"):
            self.alternates.append((values["hreflang"] or "", values.get("href") or ""))
        if tag in {"a", "link"} and values.get("href"):
            self.links.append(values["href"] or "")
        if tag in {"img", "script"} and values.get("src"):
            self.links.append(values["src"] or "")
        if tag == "script" and values.get("type") == "application/ld+json":
            self._json_parts = []
        if tag == "summary":
            self._summary_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._json_parts is not None:
            self.json_ld.append("".join(self._json_parts).strip())
            self._json_parts = None
        if tag == "summary" and self._summary_parts is not None:
            self.summaries.append("".join(self._summary_parts).strip())
            self._summary_parts = None

    def handle_data(self, data: str) -> None:
        if self._json_parts is not None:
            self._json_parts.append(data)
        if self._summary_parts is not None:
            self._summary_parts.append(data)


def local_target(raw: str) -> Path | None:
    if not raw or raw.startswith(("#", "mailto:", "tel:", "data:")):
        return None
    parsed = urlparse(raw)
    if parsed.scheme or parsed.netloc:
        return None
    path = parsed.path
    if not path:
        return None
    if path.startswith("/_vercel/"):
        return None
    candidate = ROOT / path.lstrip("/")
    if path.endswith("/"):
        candidate /= "index.html"
    return candidate


def faq_names(documents: list[dict]) -> list[str]:
    for document in documents:
        if document.get("@type") == "FAQPage":
            return [entry["name"] for entry in document.get("mainEntity", [])]
        for item in document.get("@graph", []):
            if item.get("@type") == "FAQPage":
                return [entry["name"] for entry in item.get("mainEntity", [])]
    return []


def main() -> None:
    failures: list[str] = []
    for page in sorted(ROOT.rglob("index.html")):
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        documents: list[dict] = []
        for raw in parser.json_ld:
            try:
                documents.append(json.loads(raw))
            except json.JSONDecodeError as error:
                failures.append(f"{page.relative_to(ROOT)}: invalid JSON-LD: {error}")

        if page in PRODUCT_PAGES:
            if parser.h1_count != 1:
                failures.append(f"{page.relative_to(ROOT)}: expected 1 h1, found {parser.h1_count}")
            if parser.canonical_count != 1:
                failures.append(
                    f"{page.relative_to(ROOT)}: expected 1 canonical, found {parser.canonical_count}"
                )
            schema_questions = faq_names(documents)
            if schema_questions != parser.summaries:
                failures.append(f"{page.relative_to(ROOT)}: visible FAQ and JSON-LD differ")
        elif ("x-default", "https://donalupa.com/") in parser.alternates:
            failures.append(f"{page.relative_to(ROOT)}: guide x-default points to homepage")

        for raw_link in parser.links:
            target = local_target(raw_link)
            if target is not None and not target.exists():
                failures.append(
                    f"{page.relative_to(ROOT)}: missing local target {raw_link}"
                )

    sitemap = ElementTree.parse(ROOT / "sitemap.xml")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for node in sitemap.findall("sm:url/sm:loc", namespace):
        path = urlparse(node.text or "").path
        target = ROOT / path.lstrip("/")
        if path.endswith("/"):
            target /= "index.html"
        if not target.exists():
            failures.append(f"sitemap.xml: missing target {path}")

    if failures:
        raise SystemExit("\n".join(f"ERROR: {failure}" for failure in failures))
    print("OK — HTML, JSON-LD, FAQ, internal links and sitemap are consistent")


if __name__ == "__main__":
    main()
