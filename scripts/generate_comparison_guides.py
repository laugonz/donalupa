#!/usr/bin/env python3
"""Generate the localized, independent Murdoku comparison guides."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = "https://apps.apple.com/app/id6801481670"
IMAGE = "https://donalupa.com/assets/guides/murdoku-y-dona-lupa-feature.webp"
PUBLISHED = "2026-08-26"
MODIFIED = "2026-09-13"

ALTERNATES = {
    "en": "https://donalupa.com/guides/murdoku-vs-dona-lupa/",
    "es": "https://donalupa.com/es/guias/murdoku-y-dona-lupa/",
    "fr": "https://donalupa.com/fr/guides/murdoku-et-dona-lupa/",
    "it": "https://donalupa.com/it/guide/murdoku-e-dona-lupa/",
    "pt-PT": "https://donalupa.com/pt/guias/murdoku-e-dona-lupa/",
}

PAGES = {
    "en": {
        "path": "guides/murdoku-vs-dona-lupa/index.html",
        "lang": "en",
        "home": "/",
        "guides": "/#guides",
        "guide_label": "Guides",
        "nav": ("How it works", "Cases", "Guides"),
        "nav_links": ("/#how", "/#cases", "/#guides"),
        "skip": "Skip to the comparison",
        "title": "Murdoku vs Doña Lupa: Key Differences | Doña Lupa",
        "description": "An independent Murdoku vs Doña Lupa comparison covering format, rules, tone, content and access, with links to the official sources.",
        "og_description": "An independent, sourced comparison of two different logic-puzzle games.",
        "eyebrow": "Independent comparison",
        "breadcrumb": "Murdoku vs Doña Lupa",
        "h1": "Murdoku vs Doña Lupa: what actually differs",
        "deck": "Both turn a grid and a cast of characters into a logic mystery, but they are not the same game. Murdoku is available as browser puzzles, printables and books; Doña Lupa is an independent iPhone game with outlined zones, interactive notes and short comic cases.",
        "notice": "MURDOKU is a trademark of Studios Digivoid Inc. Doña Lupa is an independent product and is not affiliated with, sponsored by or authorized by its owners. The name is used here only to identify and compare the product.",
        "alt": "Doña Lupa comparing a paper logic-puzzle book with a mobile deduction game",
        "caption": "A useful comparison starts with format and rules, not with declaring a winner.",
        "summary_label": "In one minute",
        "summary": [
            "Murdoku: web, printable puzzles and books",
            "Doña Lupa: an iPhone game",
            "Their grid rules are not identical",
            "One uses murder cases; the other uses tiny comic crimes",
            "Both offer a free way to begin",
        ],
        "format_heading": "The biggest difference is how you play",
        "format_paragraphs": [
            "The official <a href=\"https://murdoku.com/\" rel=\"noopener\">Murdoku website</a> offers puzzles to solve in a browser and cases to download and print. It also presents physical puzzle books: the first volume's official page describes 80 cases illustrated in colour. That makes Murdoku a natural fit if you like solving on paper, carrying a puzzle book or switching between web and print.",
            "<a href=\"https://apps.apple.com/app/id6801481670\">Doña Lupa</a> is designed around the iPhone. Its first interactive case introduces the mechanics on the board, notes stay inside the puzzle and the app includes a daily case. Four themed worlds group the mysteries, so progression feels closer to a mobile game than to working through a puzzle book.",
        ],
        "rules_heading": "Similar deductions, different rules",
        "rules_paragraphs": [
            "According to the <a href=\"https://murdoku.com/book\" rel=\"noopener\">official Murdoku book rules</a>, each person appears once in every row and once in every column. The guilty person must also be alone with the victim inside the same area. That final condition ties the character layout to solving the murder.",
            "In Doña Lupa, each suspect appears once per row, once per column and once per outlined zone. Every story clue is true and those clues combine with all three grid constraints to produce one solution. Both games reward elimination, but an area in Murdoku and a zone in Doña Lupa do not perform the same job, so techniques do not transfer perfectly.",
        ],
        "table_caption": "Murdoku and Doña Lupa, point by point",
        "table_headers": ("Feature", "Murdoku", "Doña Lupa"),
        "table_rows": [
            ("Format", "Web, printable puzzles and books", "iPhone app"),
            ("Structure", "One person per row and column; culprit and victim share an area alone", "One suspect per row, column and zone, plus truthful clues"),
            ("Stories", "Murder cases", "Cozy comic mysteries without bloody crimes"),
            ("Pace", "Choose a web, printable or book puzzle", "Tutorial, five difficulties, four worlds and a daily case"),
            ("Access", "Free web play and printables; paid books", "Free download and easy cases; monthly subscription or lifetime unlock"),
        ],
        "tone_heading": "Tone and presentation change the experience",
        "tone_paragraphs": [
            "Murdoku builds its premise around finding who killed the victim. Doña Lupa avoids bloody crimes: its detective may investigate a missing lunch, a suspicious dessert or a coffee-related offence. The choice is therefore not only about difficulty. It is also about the atmosphere you want between deductions.",
            "Presentation matters too. Murdoku's books work as illustrated objects you can solve at your own pace. Doña Lupa uses animated characters, interactive help and a short narrative payoff after the grid is complete. Neither approach is universally better: one favours paper and murder cases, while the other favours a phone, persistent notes and cozy humour.",
        ],
        "cta_eyebrow": "If you prefer playing on iPhone",
        "cta_heading": "Try an easy case before deciding.",
        "cta_button": "Play Doña Lupa free",
        "choice_heading": "Which one should you choose?",
        "choice_paragraph": "Choose Murdoku if you want its original cases, a physical book or a printable grid. Choose Doña Lupa if you want to solve on iPhone, receive a daily case, move through themed worlds and keep the mood light. Since both give you a free way to start, the fairest test is to play one official case from each and see which rules, pace and presentation suit you.",
        "sources": "This comparison uses information published by each product's owners and checked on 5 September 2026. Catalogues, prices and platforms may change. Check the <a href=\"https://murdoku.com/\" rel=\"noopener\">official Murdoku website</a>, its <a href=\"https://murdoku.com/book\" rel=\"noopener\">book page</a> and the <a href=\"https://apps.apple.com/app/id6801481670\">official Doña Lupa App Store listing</a> for current information. Trademark ownership can be checked in the <a href=\"https://euipo.europa.eu/eSearch/#details/trademarks/019308162\" rel=\"noopener\">EUIPO register</a>.",
        "faq_eyebrow": "Straight answers",
        "faq_heading": "Questions about the comparison",
        "faq": [
            ("Is Doña Lupa the official Murdoku app?", "No. Doña Lupa is an independent app and is not affiliated with, sponsored by or authorized by the owners of MURDOKU."),
            ("Do Murdoku and Doña Lupa use the same rules?", "No. The official Murdoku rules place one person per row and column and put the culprit alone with the victim in an area. Doña Lupa places one suspect per row, column and zone, then combines that structure with truthful story clues."),
        ],
        "related_eyebrow": "Keep investigating",
        "related_heading": "Learn Doña Lupa's rules",
        "related": [
            ("/guides/how-to-play-deduction-sudoku/", "Beginner guide", "How to play deduction sudoku", "Read the guide →"),
            ("/guides/detective-logic-grid-puzzles/", "Solving method", "How to cross clues without guessing", "Read the guide →"),
        ],
        "final_eyebrow": "Your first case is ready",
        "final_heading": "Put every suspect in the right place.",
        "final_button": "Play free on iPhone",
        "footer": "Cozy crimes, honest clues, terrible alibis.",
        "footer_links": (("Guides", "/#guides"), ("Privacy", "/privacy/"), ("Support", "/support/")),
        "language_link": ("ES", ALTERNATES["es"], "es"),
    },
    "fr": {
        "path": "fr/guides/murdoku-et-dona-lupa/index.html",
        "lang": "fr",
        "home": "/fr/",
        "guides": "/fr/#guides",
        "guide_label": "Guides",
        "nav": ("Règles", "Affaires", "Guides"),
        "nav_links": ("/fr/#regles", "/fr/#affaires", "/fr/#guides"),
        "skip": "Aller à la comparaison",
        "title": "Murdoku et Doña Lupa : les différences | Doña Lupa",
        "description": "Comparaison indépendante entre Murdoku et Doña Lupa : formats, règles, ambiance, contenu et accès, avec les sources officielles.",
        "og_description": "Une comparaison indépendante et sourcée de deux jeux de logique différents.",
        "eyebrow": "Comparaison indépendante",
        "breadcrumb": "Murdoku et Doña Lupa",
        "h1": "Murdoku et Doña Lupa : ce qui change vraiment",
        "deck": "Les deux jeux transforment une grille et des personnages en enquête logique, mais ce ne sont pas les mêmes jeux. Murdoku existe sur le web, en fiches imprimables et en livres ; Doña Lupa est une app indépendante pour iPhone avec des zones, des notes interactives et de petites affaires comiques.",
        "notice": "MURDOKU est une marque de Studios Digivoid Inc. Doña Lupa est un produit indépendant, sans affiliation, parrainage ni autorisation de ses titulaires. Le nom est utilisé ici uniquement pour identifier et comparer le produit.",
        "alt": "Doña Lupa compare un livre de jeux logiques sur papier et une app mobile de déduction",
        "caption": "Une comparaison utile commence par le format et les règles, pas par la désignation d'un vainqueur.",
        "summary_label": "En une minute",
        "summary": ["Murdoku : web, fiches imprimables et livres", "Doña Lupa : app pour iPhone", "Les règles de grille ne sont pas identiques", "L'un enquête sur des meurtres, l'autre sur de petits délits comiques", "Les deux permettent de commencer gratuitement"],
        "format_heading": "La principale différence : la façon de jouer",
        "format_paragraphs": [
            "Le <a href=\"https://murdoku.com/\" rel=\"noopener\">site officiel de Murdoku</a> propose des grilles à résoudre dans le navigateur et des affaires à télécharger puis imprimer. Il présente également des livres physiques : la page officielle du premier volume annonce 80 affaires illustrées en couleur. Murdoku convient donc naturellement aux personnes qui aiment résoudre sur papier, emporter un livre de jeux ou alterner entre web et impression.",
            "<a href=\"https://apps.apple.com/fr/app/id6801481670\">Doña Lupa</a> est pensée pour l'iPhone. Sa première affaire interactive présente les mécaniques directement sur la grille, les notes restent dans la partie et l'app propose une affaire quotidienne. Quatre univers thématiques organisent les enquêtes, ce qui donne une progression proche d'un jeu mobile plutôt que d'un cahier de grilles.",
        ],
        "rules_heading": "Des déductions proches, des règles différentes",
        "rules_paragraphs": [
            "Selon les <a href=\"https://murdoku.com/book\" rel=\"noopener\">règles officielles du livre Murdoku</a>, chaque personne apparaît une fois par ligne et une fois par colonne. La personne coupable doit aussi se retrouver seule avec la victime dans la même zone. Cette dernière condition relie la disposition des personnages à la résolution du meurtre.",
            "Dans Doña Lupa, chaque suspect apparaît une fois par ligne, par colonne et par zone délimitée. Tous les indices narratifs sont vrais et s'ajoutent à ces trois contraintes pour conduire à une solution unique. Les deux jeux récompensent l'élimination, mais une zone de Murdoku et une zone de Doña Lupa n'ont pas la même fonction.",
        ],
        "table_caption": "Murdoku et Doña Lupa, point par point",
        "table_headers": ("Critère", "Murdoku", "Doña Lupa"),
        "table_rows": [("Format", "Web, grilles imprimables et livres", "App pour iPhone"), ("Structure", "Une personne par ligne et colonne ; coupable et victime seuls dans une zone", "Un suspect par ligne, colonne et zone, plus des indices vrais"), ("Histoires", "Affaires de meurtre", "Mystères cosy et comiques, sans crime sanglant"), ("Rythme", "Choix d'une grille web, imprimée ou dans un livre", "Tutoriel, cinq difficultés, quatre univers et affaire quotidienne"), ("Accès", "Jeu web et imprimables gratuits ; livres payants", "Téléchargement et affaires faciles gratuits ; abonnement mensuel ou achat à vie")],
        "tone_heading": "L'ambiance et la présentation changent l'expérience",
        "tone_paragraphs": [
            "Murdoku fonde son intrigue sur l'identification de la personne qui a tué la victime. Doña Lupa évite les crimes sanglants : son enquêtrice cherche plutôt qui a fait disparaître un déjeuner, trafiqué un dessert ou rendu un café suspect. Le choix ne dépend donc pas seulement de la difficulté, mais aussi de l'ambiance recherchée.",
            "La présentation compte également. Les livres de Murdoku sont des objets illustrés à résoudre à son rythme. Doña Lupa utilise des personnages animés, des aides interactives et une petite chute narrative lorsque la grille est terminée. Aucune formule n'est supérieure dans l'absolu : l'une privilégie le papier et le meurtre, l'autre le téléphone et l'humour cosy.",
        ],
        "cta_eyebrow": "Si tu préfères jouer sur iPhone",
        "cta_heading": "Essaie une affaire facile avant de choisir.",
        "cta_button": "Jouer gratuitement à Doña Lupa",
        "choice_heading": "Lequel choisir ?",
        "choice_paragraph": "Choisis Murdoku si tu recherches ses affaires originales, un livre physique ou une grille à imprimer. Choisis Doña Lupa si tu veux résoudre sur iPhone, recevoir une affaire quotidienne, avancer dans plusieurs univers et garder une ambiance légère. Les deux proposant une façon gratuite de commencer, le test le plus juste consiste à essayer une affaire officielle de chacun.",
        "sources": "Cette comparaison repose sur les informations publiées par les responsables de chaque produit et vérifiées le 5 septembre 2026. Les catalogues, prix et plateformes peuvent évoluer. Consulte le <a href=\"https://murdoku.com/\" rel=\"noopener\">site officiel de Murdoku</a>, sa <a href=\"https://murdoku.com/book\" rel=\"noopener\">page consacrée aux livres</a> et la <a href=\"https://apps.apple.com/fr/app/id6801481670\">fiche App Store officielle de Doña Lupa</a>. La marque peut être vérifiée dans le <a href=\"https://euipo.europa.eu/eSearch/#details/trademarks/019308162\" rel=\"noopener\">registre de l'EUIPO</a>.",
        "faq_eyebrow": "Réponses claires",
        "faq_heading": "Questions sur la comparaison",
        "faq": [("Doña Lupa est-elle l'app officielle de Murdoku ?", "Non. Doña Lupa est une app indépendante, sans affiliation, parrainage ni autorisation des titulaires de MURDOKU."), ("Murdoku et Doña Lupa ont-ils les mêmes règles ?", "Non. Les règles officielles de Murdoku placent une personne par ligne et colonne et le coupable seul avec la victime dans une zone. Doña Lupa place un suspect par ligne, colonne et zone, puis ajoute des indices narratifs vrais.")],
        "related_eyebrow": "Poursuivre l'enquête",
        "related_heading": "Apprendre les règles de Doña Lupa",
        "related": [("/fr/guides/comment-jouer-au-sudoku-de-deduction/", "Guide pour débuter", "Comment jouer au sudoku de déduction", "Lire le guide →"), ("/fr/guides/jeux-de-detective-a-grille-logique/", "Méthode de résolution", "Croiser les indices sans deviner", "Lire le guide →")],
        "final_eyebrow": "Ta première affaire est prête",
        "final_heading": "Place chaque suspect au bon endroit.",
        "final_button": "Jouer gratuitement sur iPhone",
        "footer": "Crimes cosy, indices honnêtes, alibis déplorables.",
        "footer_links": (("Guides", "/fr/#guides"), ("Confidentialité", "/privacy/"), ("Assistance", "/support/")),
        "language_link": ("EN", ALTERNATES["en"], "en"),
    },
    "it": {
        "path": "it/guide/murdoku-e-dona-lupa/index.html",
        "lang": "it",
        "home": "/it/",
        "guides": "/it/#guide",
        "guide_label": "Guide",
        "nav": ("Come funziona", "Casi", "Guide"),
        "nav_links": ("/it/#come", "/it/#casi", "/it/#guide"),
        "skip": "Vai al confronto",
        "title": "Murdoku e Doña Lupa: le differenze | Doña Lupa",
        "description": "Confronto indipendente tra Murdoku e Doña Lupa: formati, regole, atmosfera, contenuti e accesso, con fonti ufficiali.",
        "og_description": "Un confronto indipendente e documentato tra due giochi di logica diversi.",
        "eyebrow": "Confronto indipendente",
        "breadcrumb": "Murdoku e Doña Lupa",
        "h1": "Murdoku e Doña Lupa: cosa cambia davvero",
        "deck": "Entrambi trasformano una griglia e un gruppo di personaggi in un mistero logico, ma non sono lo stesso gioco. Murdoku è disponibile sul web, come puzzle stampabile e in volume; Doña Lupa è un'app indipendente per iPhone con zone, note interattive e piccoli casi comici.",
        "notice": "MURDOKU è un marchio di Studios Digivoid Inc. Doña Lupa è un prodotto indipendente e non è affiliato, sponsorizzato o autorizzato dai suoi titolari. Il nome è usato qui soltanto per identificare e confrontare il prodotto.",
        "alt": "Doña Lupa confronta un libro cartaceo di puzzle logici con un gioco mobile di deduzione",
        "caption": "Un confronto utile parte dal formato e dalle regole, non dalla ricerca di un vincitore.",
        "summary_label": "In un minuto",
        "summary": ["Murdoku: web, puzzle stampabili e libri", "Doña Lupa: app per iPhone", "Le regole della griglia non sono identiche", "Uno propone omicidi, l'altra piccoli crimini comici", "Entrambi permettono di iniziare gratis"],
        "format_heading": "La differenza principale è come si gioca",
        "format_paragraphs": [
            "Il <a href=\"https://murdoku.com/\" rel=\"noopener\">sito ufficiale di Murdoku</a> propone puzzle da risolvere nel browser e casi da scaricare e stampare. Presenta anche libri fisici: la pagina ufficiale del primo volume indica 80 casi illustrati a colori. È quindi adatto a chi ama risolvere su carta, portare con sé un libro di enigmi o alternare tra web e stampa.",
            "<a href=\"https://apps.apple.com/it/app/id6801481670\">Doña Lupa</a> è progettata per iPhone. Il primo caso interattivo introduce le meccaniche direttamente sul tabellone, le note restano nella partita e l'app include un caso giornaliero. Quattro mondi tematici raccolgono i misteri, con una progressione più vicina a un gioco mobile che a un quaderno di puzzle.",
        ],
        "rules_heading": "Deduzioni simili, regole diverse",
        "rules_paragraphs": [
            "Secondo le <a href=\"https://murdoku.com/book\" rel=\"noopener\">regole ufficiali del libro Murdoku</a>, ogni persona compare una volta in ogni riga e in ogni colonna. La persona colpevole deve inoltre trovarsi da sola con la vittima nella stessa area. Questa condizione collega la disposizione dei personaggi alla soluzione dell'omicidio.",
            "In Doña Lupa ogni sospetto compare una volta per riga, una volta per colonna e una volta per zona delimitata. Tutti gli indizi narrativi sono veri e si combinano con i tre vincoli per produrre una sola soluzione. Entrambi premiano l'eliminazione, ma l'area di Murdoku e la zona di Doña Lupa hanno funzioni diverse.",
        ],
        "table_caption": "Murdoku e Doña Lupa, punto per punto",
        "table_headers": ("Aspetto", "Murdoku", "Doña Lupa"),
        "table_rows": [("Formato", "Web, puzzle stampabili e libri", "App per iPhone"), ("Struttura", "Una persona per riga e colonna; colpevole e vittima soli in un'area", "Un sospetto per riga, colonna e zona, più indizi veri"), ("Storie", "Casi di omicidio", "Misteri comici e accoglienti, senza crimini cruenti"), ("Ritmo", "Scelta tra puzzle web, stampato o del libro", "Tutorial, cinque difficoltà, quattro mondi e caso giornaliero"), ("Accesso", "Gioco web e stampabili gratuiti; libri a pagamento", "Download e casi facili gratuiti; abbonamento mensile o acquisto a vita")],
        "tone_heading": "Atmosfera e presentazione cambiano l'esperienza",
        "tone_paragraphs": [
            "Murdoku costruisce la sua premessa intorno alla ricerca di chi ha ucciso la vittima. Doña Lupa evita i crimini cruenti: l'investigatrice può cercare chi ha fatto sparire un pranzo, manomesso un dolce o reso sospetto un caffè. La scelta non riguarda quindi solo la difficoltà, ma anche l'atmosfera che desideri.",
            "Anche la presentazione conta. I libri di Murdoku sono oggetti illustrati da risolvere al proprio ritmo. Doña Lupa usa personaggi animati, aiuti interattivi e una breve conclusione narrativa quando completi la griglia. Nessuna formula è migliore in assoluto: una privilegia carta e omicidi, l'altra telefono e umorismo accogliente.",
        ],
        "cta_eyebrow": "Se preferisci giocare su iPhone",
        "cta_heading": "Prova un caso facile prima di scegliere.",
        "cta_button": "Gioca gratis a Doña Lupa",
        "choice_heading": "Quale scegliere?",
        "choice_paragraph": "Scegli Murdoku se cerchi i suoi casi originali, un libro fisico o una griglia da stampare. Scegli Doña Lupa se vuoi risolvere su iPhone, ricevere un caso giornaliero, avanzare tra mondi diversi e mantenere un tono leggero. Poiché entrambi offrono un modo gratuito per iniziare, la prova più corretta è giocare un caso ufficiale di ciascuno.",
        "sources": "Questo confronto usa informazioni pubblicate dai responsabili dei due prodotti e verificate il 5 settembre 2026. Cataloghi, prezzi e piattaforme possono cambiare. Consulta il <a href=\"https://murdoku.com/\" rel=\"noopener\">sito ufficiale di Murdoku</a>, la sua <a href=\"https://murdoku.com/book\" rel=\"noopener\">pagina dei libri</a> e la <a href=\"https://apps.apple.com/it/app/id6801481670\">pagina ufficiale di Doña Lupa su App Store</a>. La titolarità del marchio è verificabile nel <a href=\"https://euipo.europa.eu/eSearch/#details/trademarks/019308162\" rel=\"noopener\">registro EUIPO</a>.",
        "faq_eyebrow": "Risposte chiare",
        "faq_heading": "Domande sul confronto",
        "faq": [("Doña Lupa è l'app ufficiale di Murdoku?", "No. Doña Lupa è un'app indipendente e non è affiliata, sponsorizzata o autorizzata dai titolari di MURDOKU."), ("Murdoku e Doña Lupa hanno le stesse regole?", "No. Le regole ufficiali di Murdoku prevedono una persona per riga e colonna e il colpevole da solo con la vittima in un'area. Doña Lupa inserisce un sospetto per riga, colonna e zona e aggiunge indizi narrativi veri.")],
        "related_eyebrow": "Continua a indagare",
        "related_heading": "Impara le regole di Doña Lupa",
        "related": [("/it/guide/come-giocare-sudoku-deduzione/", "Guida per iniziare", "Come giocare al sudoku investigativo", "Leggi la guida →"), ("/it/guide/giochi-investigativi-con-griglia-logica/", "Metodo di soluzione", "Come incrociare gli indizi senza tentativi", "Leggi la guida →")],
        "final_eyebrow": "Il tuo primo caso è pronto",
        "final_heading": "Metti ogni sospetto al posto giusto.",
        "final_button": "Gioca gratis su iPhone",
        "footer": "Piccoli crimini, indizi sinceri, pessimi alibi.",
        "footer_links": (("Guide", "/it/#guide"), ("Privacy", "/privacy/"), ("Supporto", "/support/")),
        "language_link": ("EN", ALTERNATES["en"], "en"),
    },
    "pt-PT": {
        "path": "pt/guias/murdoku-e-dona-lupa/index.html",
        "lang": "pt-PT",
        "home": "/pt/",
        "guides": "/pt/#guias",
        "guide_label": "Guias",
        "nav": ("Como funciona", "Casos", "Guias"),
        "nav_links": ("/pt/#como", "/pt/#casos", "/pt/#guias"),
        "skip": "Saltar para a comparação",
        "title": "Murdoku e Doña Lupa: diferenças reais | Doña Lupa",
        "description": "Comparação independente entre Murdoku e Doña Lupa: formatos, regras, ambiente, conteúdos e acesso, com fontes oficiais.",
        "og_description": "Uma comparação independente e documentada entre dois jogos de lógica diferentes.",
        "eyebrow": "Comparação independente",
        "breadcrumb": "Murdoku e Doña Lupa",
        "h1": "Murdoku e Doña Lupa: o que muda realmente",
        "deck": "Ambos transformam uma grelha e um elenco de personagens num mistério lógico, mas não são o mesmo jogo. Murdoku existe na web, em puzzles para imprimir e em livros; Doña Lupa é uma app independente para iPhone com zonas, notas interativas e pequenos casos cómicos.",
        "notice": "MURDOKU é uma marca da Studios Digivoid Inc. Doña Lupa é um produto independente e não é afiliado, patrocinado nem autorizado pelos seus titulares. O nome é usado aqui apenas para identificar e comparar o produto.",
        "alt": "Doña Lupa compara um livro de puzzles lógicos em papel com um jogo móvel de dedução",
        "caption": "Uma comparação útil começa pelo formato e pelas regras, não pela escolha de um vencedor.",
        "summary_label": "Num minuto",
        "summary": ["Murdoku: web, puzzles para imprimir e livros", "Doña Lupa: app para iPhone", "As regras da grelha não são idênticas", "Um investiga homicídios; o outro, pequenos crimes cómicos", "Ambos permitem começar gratuitamente"],
        "format_heading": "A principal diferença está na forma de jogar",
        "format_paragraphs": [
            "O <a href=\"https://murdoku.com/\" rel=\"noopener\">site oficial de Murdoku</a> disponibiliza puzzles para resolver no navegador e casos para descarregar e imprimir. Também apresenta livros físicos: a página oficial do primeiro volume indica 80 casos ilustrados a cores. É uma opção natural para quem gosta de resolver em papel, levar um livro de passatempos ou alternar entre a web e a impressão.",
            "<a href=\"https://apps.apple.com/pt/app/id6801481670\">Doña Lupa</a> foi concebida para iPhone. O primeiro caso interativo apresenta as mecânicas no próprio tabuleiro, as notas ficam guardadas na partida e a app inclui um caso diário. Quatro mundos temáticos agrupam os mistérios, por isso a progressão se aproxima mais de um jogo móvel do que de um caderno de puzzles.",
        ],
        "rules_heading": "Deduções semelhantes, regras diferentes",
        "rules_paragraphs": [
            "Segundo as <a href=\"https://murdoku.com/book\" rel=\"noopener\">regras oficiais do livro Murdoku</a>, cada pessoa aparece uma vez em cada linha e uma vez em cada coluna. A pessoa culpada também tem de ficar a sós com a vítima dentro da mesma área. Esta condição liga a colocação das personagens à resolução do homicídio.",
            "Em Doña Lupa, cada suspeito aparece uma vez por linha, uma vez por coluna e uma vez por zona delimitada. Todas as pistas narrativas são verdadeiras e juntam-se a estas três restrições para criar uma única solução. Ambos valorizam a eliminação, mas uma área de Murdoku e uma zona de Doña Lupa não cumprem a mesma função.",
        ],
        "table_caption": "Murdoku e Doña Lupa, ponto por ponto",
        "table_headers": ("Aspeto", "Murdoku", "Doña Lupa"),
        "table_rows": [("Formato", "Web, puzzles para imprimir e livros", "App para iPhone"), ("Estrutura", "Uma pessoa por linha e coluna; culpado e vítima a sós numa área", "Um suspeito por linha, coluna e zona, mais pistas verdadeiras"), ("Histórias", "Casos de homicídio", "Mistérios cómicos e acolhedores, sem crimes sangrentos"), ("Ritmo", "Escolha entre puzzle web, impresso ou do livro", "Tutorial, cinco dificuldades, quatro mundos e caso diário"), ("Acesso", "Jogo web e imprimíveis gratuitos; livros pagos", "Download e casos fáceis gratuitos; subscrição mensal ou compra vitalícia")],
        "tone_heading": "O ambiente e a apresentação mudam a experiência",
        "tone_paragraphs": [
            "Murdoku constrói a premissa à volta da descoberta de quem matou a vítima. Doña Lupa evita crimes sangrentos: a detetive pode investigar quem fez desaparecer um almoço, alterou uma sobremesa ou tornou um café suspeito. A escolha não depende apenas da dificuldade, mas também do ambiente que procuras.",
            "A apresentação também conta. Os livros de Murdoku são objetos ilustrados para resolver ao teu ritmo. Doña Lupa usa personagens animadas, ajudas interativas e um pequeno desfecho narrativo quando completas a grelha. Nenhuma fórmula é sempre melhor: uma privilegia papel e homicídios, a outra telemóvel e humor acolhedor.",
        ],
        "cta_eyebrow": "Se preferes jogar no iPhone",
        "cta_heading": "Experimenta um caso fácil antes de escolher.",
        "cta_button": "Jogar Doña Lupa gratuitamente",
        "choice_heading": "Qual deves escolher?",
        "choice_paragraph": "Escolhe Murdoku se procuras os seus casos originais, um livro físico ou uma grelha para imprimir. Escolhe Doña Lupa se queres resolver no iPhone, receber um caso diário, avançar por vários mundos e manter um tom leve. Como ambos oferecem uma forma gratuita de começar, o teste mais justo é jogar um caso oficial de cada um.",
        "sources": "Esta comparação usa informações publicadas pelos responsáveis de cada produto e verificadas em 5 de setembro de 2026. Catálogos, preços e plataformas podem mudar. Consulta o <a href=\"https://murdoku.com/\" rel=\"noopener\">site oficial de Murdoku</a>, a sua <a href=\"https://murdoku.com/book\" rel=\"noopener\">página dos livros</a> e a <a href=\"https://apps.apple.com/pt/app/id6801481670\">página oficial de Doña Lupa na App Store</a>. A titularidade da marca pode ser verificada no <a href=\"https://euipo.europa.eu/eSearch/#details/trademarks/019308162\" rel=\"noopener\">registo da EUIPO</a>.",
        "faq_eyebrow": "Respostas claras",
        "faq_heading": "Perguntas sobre a comparação",
        "faq": [("Doña Lupa é a app oficial de Murdoku?", "Não. Doña Lupa é uma app independente e não é afiliada, patrocinada nem autorizada pelos titulares de MURDOKU."), ("Murdoku e Doña Lupa têm as mesmas regras?", "Não. As regras oficiais de Murdoku colocam uma pessoa por linha e coluna e o culpado a sós com a vítima numa área. Doña Lupa coloca um suspeito por linha, coluna e zona e acrescenta pistas narrativas verdadeiras.")],
        "related_eyebrow": "Continua a investigar",
        "related_heading": "Aprende as regras de Doña Lupa",
        "related": [("/pt/guias/como-jogar-sudoku-de-deducao/", "Guia para começar", "Como jogar sudoku de dedução", "Ler o guia →"), ("/pt/guias/jogos-de-detetive-com-grelha-logica/", "Método de resolução", "Como cruzar pistas sem adivinhar", "Ler o guia →")],
        "final_eyebrow": "O teu primeiro caso está pronto",
        "final_heading": "Coloca cada suspeito no lugar certo.",
        "final_button": "Jogar gratuitamente no iPhone",
        "footer": "Crimes acolhedores, pistas honestas, péssimos álibis.",
        "footer_links": (("Guias", "/pt/#guias"), ("Privacidade", "/privacy/"), ("Apoio", "/support/")),
        "language_link": ("EN", ALTERNATES["en"], "en"),
    },
}


def hreflang_links() -> str:
    links = [
        f'<link rel="alternate" hreflang="{lang}" href="{url}">'
        for lang, url in ALTERNATES.items()
    ]
    links.append(
        f'<link rel="alternate" hreflang="x-default" href="{ALTERNATES["en"]}">'
    )
    return "\n  ".join(links)


def render(locale: str, data: dict) -> str:
    esc = html.escape
    canonical = ALTERNATES[locale]
    faq_schema = [
        {
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {"@type": "Answer", "text": answer},
        }
        for question, answer in data["faq"]
    ]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": data["h1"],
                "description": data["description"],
                "image": IMAGE,
                "datePublished": PUBLISHED,
                "dateModified": MODIFIED,
                "inLanguage": data["lang"],
                "author": {"@type": "Person", "name": "Laura González"},
                "publisher": {
                    "@type": "Organization",
                    "name": "Doña Lupa",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://donalupa.com/assets/app-icon.png",
                    },
                },
                "mainEntityOfPage": canonical,
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Doña Lupa",
                        "item": f"https://donalupa.com{data['home']}",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": data["guide_label"],
                        "item": f"https://donalupa.com{data['guides']}",
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": data["breadcrumb"],
                        "item": canonical,
                    },
                ],
            },
            {"@type": "FAQPage", "mainEntity": faq_schema},
        ],
    }
    nav = "".join(
        f'<a href="{href}">{esc(label)}</a>'
        for label, href in zip(data["nav"], data["nav_links"])
    )
    summary = "".join(f"<li>{esc(item)}</li>" for item in data["summary"])
    format_paragraphs = "".join(f"<p>{paragraph}</p>" for paragraph in data["format_paragraphs"])
    rules_paragraphs = "".join(f"<p>{paragraph}</p>" for paragraph in data["rules_paragraphs"])
    tone_paragraphs = "".join(f"<p>{paragraph}</p>" for paragraph in data["tone_paragraphs"])
    rows = "".join(
        f'<tr><th scope="row">{esc(label)}</th><td>{esc(murdoku)}</td><td>{esc(dona)}</td></tr>'
        for label, murdoku, dona in data["table_rows"]
    )
    faq = "".join(
        f"<details><summary>{esc(question)}</summary><p>{esc(answer)}</p></details>"
        for question, answer in data["faq"]
    )
    related = "".join(
        f'<a href="{href}"><span>{esc(label)}</span><strong>{esc(title)}</strong><small>{esc(cta)}</small></a>'
        for href, label, title, cta in data["related"]
    )
    footer_links = "".join(
        f'<a href="{href}">{esc(label)}</a>' for label, href in data["footer_links"]
    )
    th1, th2, th3 = data["table_headers"]
    language_label, language_url, language_code = data["language_link"]

    return f'''<!DOCTYPE html>
<html lang="{data['lang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(data['title'])}</title>
  <meta name="description" content="{esc(data['description'])}">
  <meta name="theme-color" content="#f4ecd7">
  <meta name="apple-itunes-app" content="app-id=6801481670">
  <link rel="canonical" href="{canonical}">
  {hreflang_links()}
  <link rel="icon" href="/assets/app-icon.png">
  <link rel="stylesheet" href="/_style.css?v=20260826-4">
  <link rel="preload" as="image" href="/assets/guides/murdoku-y-dona-lupa-feature.webp" fetchpriority="high">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Doña Lupa">
  <meta property="og:title" content="{esc(data['h1'])}">
  <meta property="og:description" content="{esc(data['og_description'])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{IMAGE}">
  <meta property="og:image:alt" content="{esc(data['alt'])}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(data['h1'])}">
  <meta name="twitter:description" content="{esc(data['og_description'])}">
  <meta name="twitter:image" content="{IMAGE}">
  <script type="application/ld+json">{json.dumps(graph, ensure_ascii=False)}</script>
  <script>window.va=window.va||function(){{(window.vaq=window.vaq||[]).push(arguments);}};</script>
  <script defer src="/_vercel/insights/script.js"></script>
</head>
<body class="guide-page comparison-page">
  <a class="skip-link" href="#article">{esc(data['skip'])}</a>
  <header class="site-header"><div class="container nav-shell"><a class="brand" href="{data['home']}" aria-label="Doña Lupa"><img src="/assets/app-icon.png" width="44" height="44" alt=""><span>Doña Lupa</span></a><nav aria-label="{esc(data['guide_label'])}">{nav}<a class="language-link" href="{language_url}" lang="{language_code}" hreflang="{language_code}">{language_label}</a></nav></div></header>

  <main id="article"><article>
    <header class="guide-hero container">
      <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{data['home']}">Doña Lupa</a><span aria-hidden="true">/</span><a href="{data['guides']}">{esc(data['guide_label'])}</a><span aria-hidden="true">/</span><span>{esc(data['breadcrumb'])}</span></nav>
      <p class="eyebrow">{esc(data['eyebrow'])}</p>
      <h1>{esc(data['h1'])}</h1>
      <p class="guide-deck"><strong>{esc(data['deck'].split('. ', 1)[0])}.</strong> {esc(data['deck'].split('. ', 1)[1])}</p>
      <div class="trademark-notice" role="note"><strong>{esc(data['eyebrow'])}:</strong> {esc(data['notice'])}</div>
      <figure class="guide-feature"><img src="/assets/guides/murdoku-y-dona-lupa-feature.webp" width="1536" height="1024" fetchpriority="high" alt="{esc(data['alt'])}"><figcaption>{esc(data['caption'])}</figcaption></figure>
    </header>

    <div class="guide-layout container">
      <aside class="key-points" aria-label="{esc(data['summary_label'])}"><p class="eyebrow">{esc(data['summary_label'])}</p><ul>{summary}</ul></aside>
      <div class="guide-body">
        <h2>{esc(data['format_heading'])}</h2>{format_paragraphs}
        <h2>{esc(data['rules_heading'])}</h2>{rules_paragraphs}
        <div class="comparison-table-wrap"><table class="comparison-table"><caption>{esc(data['table_caption'])}</caption><thead><tr><th scope="col">{esc(th1)}</th><th scope="col">{esc(th2)}</th><th scope="col">{esc(th3)}</th></tr></thead><tbody>{rows}</tbody></table></div>
        <h2>{esc(data['tone_heading'])}</h2>{tone_paragraphs}
        <div class="article-cta"><div><p class="eyebrow">{esc(data['cta_eyebrow'])}</p><h2>{esc(data['cta_heading'])}</h2></div><a class="button button-primary" href="{APP}">{esc(data['cta_button'])} <span aria-hidden="true">↗</span></a></div>
        <h2>{esc(data['choice_heading'])}</h2><p>{esc(data['choice_paragraph'])}</p><p>{data['sources']}</p>
        <section class="article-faq" aria-labelledby="guide-faq-title"><p class="eyebrow">{esc(data['faq_eyebrow'])}</p><h2 id="guide-faq-title">{esc(data['faq_heading'])}</h2>{faq}</section>
      </div>
    </div>

    <section class="related-guides container" aria-labelledby="related-title"><p class="eyebrow">{esc(data['related_eyebrow'])}</p><h2 id="related-title">{esc(data['related_heading'])}</h2><div class="related-grid">{related}</div></section>
  </article>
  <section class="final-cta"><div class="container final-cta-inner"><img src="/assets/app-icon.png" width="112" height="112" alt="Doña Lupa"><div><p class="eyebrow">{esc(data['final_eyebrow'])}</p><h2>{esc(data['final_heading'])}</h2></div><a class="button button-primary" href="{APP}">{esc(data['final_button'])} <span aria-hidden="true">↗</span></a></div></section></main>

  <footer class="site-footer"><div class="container footer-inner"><a class="brand footer-brand" href="{data['home']}"><img src="/assets/app-icon.png" width="36" height="36" alt="">Doña Lupa</a><p>{esc(data['footer'])}</p><nav aria-label="{esc(data['guide_label'])}">{footer_links}</nav><small>© 2026 Laura González</small></div></footer>
</body>
</html>
'''


for locale, page in PAGES.items():
    target = ROOT / page["path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(locale, page), encoding="utf-8")
    print(target.relative_to(ROOT))
