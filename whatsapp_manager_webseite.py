from __future__ import annotations

from nicegui import ui


GITHUB_URL = "https://github.com/xinyulyuonline/WhatsApp-Manager"
BRAND = "WhatsApp Manager"

LANGUAGES = {
    "en": {
        "language": "Language",
        "nav_subtitle": "Open Source WhatsApp Automation",
        "github": "GitHub",
        "eyebrow": "Python, Selenium and WhatsApp Web",
        "hero_copy": (
            "A professional open-source service that monitors WhatsApp groups, detects commands "
            "and answers important test and assignment information instantly. Built for reliable "
            "operation on Windows, Linux and Raspberry Pi."
        ),
        "download": "Download project",
        "repo": "View repository",
        "mockup_chats": "Chats",
        "mockup_items": [
            ("Group 8a", "New message: /KA", True),
            ("Math Project", "Today, 17:10", False),
            ("Info Channel", "Yesterday", False),
            ("Class Planning", "Friday", False),
        ],
        "mockup_messages": [
            ("in", "Can someone send the test list again?"),
            ("in", "/KA"),
            ("out", "Current test entries:\nMath: functions, Friday\nGerman: essay writing, Monday"),
            ("in", "/addKA English vocabulary test Tuesday"),
            ("out", "Saved: English vocabulary test Tuesday"),
        ],
        "metrics_title": "Automation that saves real time every day",
        "metrics_copy": (
            "WhatsApp Manager reduces repeated questions in groups, manages test entries in simple "
            "text files and stays transparent through clear configuration."
        ),
        "metrics": [
            ("0.5s", "configurable polling for fast reactions"),
            ("3", "core commands for listing, adding and deleting"),
            ("24/7", "ready for continuous Raspberry Pi operation"),
            ("100%", "open, auditable and self-hostable"),
        ],
        "features_title": "Why this service stands out",
        "features": [
            ("bolt", "#1fa855", "Fast answers", "New messages are read regularly and matching commands are answered automatically."),
            ("playlist_add", "#2563eb", "Manage the test list", "/addKA and /delKA update entries directly from the group chat."),
            ("settings", "#087f8c", "Clean configuration", "Group name, commands, files, browser paths and headless mode live in config.ini."),
            ("memory", "#f2b84b", "Raspberry Pi ready", "A service file and install script help with long-running operation on small hardware."),
            ("verified_user", "#e25563", "Controlled access", "Blocked names and own-message handling can be adjusted in settings."),
            ("public", "#374151", "Open source", "The code can be inspected, adapted and downloaded from GitHub."),
        ],
        "install_title": "From download to always-on service",
        "install_copy": (
            "The project stays intentionally lean: create a Python environment, install dependencies, "
            "adjust the configuration and start the bot."
        ),
        "install_box_title": "Start in a few commands",
        "github_open": "Open on GitHub",
        "chart_title": "Example weekly relief",
        "chart_copy": "Fewer repeated replies, faster answers and clearer test information.",
        "chart_bar": "Manually answered questions",
        "chart_line": "With WhatsApp Manager",
        "chart_days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "architecture_title": "Architecture at a glance",
        "architecture_copy": (
            "The app separates configuration, WhatsApp Web automation and simple text files. "
            "That makes it easy to understand, deploy and extend."
        ),
        "workflow_title": "Runtime workflow",
        "workflow_copy": "The service stays simple: read, check, update, reply.",
        "workflow_steps": [
            ("login", "WhatsApp Web", "Scan the QR code once"),
            ("groups", "Open group", "Target group from config.ini"),
            ("search", "Detect command", "/KA, /addKA or /delKA"),
            ("edit_note", "Maintain files", "Reply and test list"),
            ("send", "Send answer", "Directly into the chat"),
        ],
        "system_title": "System building blocks",
        "system_copy": "A compact structure for understandable automation.",
        "system_parts": ["Selenium Bot", "config.ini", "KA files", "WhatsApp Web", "systemd"],
        "footer": "WhatsApp Manager is an open-source project by xinyulyuonline.",
    },
    "de": {
        "language": "Sprache",
        "nav_subtitle": "Open-Source WhatsApp-Automatisierung",
        "github": "GitHub",
        "eyebrow": "Python, Selenium und WhatsApp Web",
        "hero_copy": (
            "Ein professioneller Open-Source-Service, der WhatsApp-Gruppen automatisch beobachtet, "
            "Befehle erkennt und wichtige KA-Informationen sofort beantwortet. Entwickelt fuer "
            "zuverlaessigen Betrieb auf Windows, Linux und Raspberry Pi."
        ),
        "download": "Projekt herunterladen",
        "repo": "Repository ansehen",
        "mockup_chats": "Chats",
        "mockup_items": [
            ("Gruppe 8a", "Neue Nachricht: /KA", True),
            ("Mathe Projekt", "Heute, 17:10", False),
            ("Info Kanal", "Gestern", False),
            ("Klassenplanung", "Freitag", False),
        ],
        "mockup_messages": [
            ("in", "Kann jemand bitte nochmal die KA-Liste schicken?"),
            ("in", "/KA"),
            ("out", "Aktuelle KA-Eintraege:\nMathe: Funktionen, Freitag\nDeutsch: Argumentation, Montag"),
            ("in", "/addKA Englisch Vokabeltest Dienstag"),
            ("out", "Gespeichert: Englisch Vokabeltest Dienstag"),
        ],
        "metrics_title": "Automatisierung, die im Alltag wirklich Arbeit spart",
        "metrics_copy": (
            "Der WhatsApp Manager reduziert wiederholte Fragen in Gruppen, verwaltet KA-Eintraege "
            "in einfachen Textdateien und bleibt durch Konfiguration transparent wartbar."
        ),
        "metrics": [
            ("0.5s", "konfigurierbares Polling fuer schnelle Reaktionen"),
            ("3", "Kernbefehle fuer Anzeigen, Hinzufuegen und Loeschen"),
            ("24/7", "geeignet fuer dauerhaften Raspberry-Pi-Betrieb"),
            ("100%", "offen einsehbar und selbst hostbar"),
        ],
        "features_title": "Warum dieser Service ueberzeugt",
        "features": [
            ("bolt", "#1fa855", "Schnelle Antworten", "Neue Nachrichten werden regelmaessig gelesen und passende Befehle automatisch beantwortet."),
            ("playlist_add", "#2563eb", "KA-Liste pflegen", "Mit /addKA und /delKA lassen sich Eintraege direkt aus der Gruppe aktualisieren."),
            ("settings", "#087f8c", "Sauber konfigurierbar", "Gruppe, Befehle, Dateien, Browserpfade und Headless-Modus liegen in config.ini."),
            ("memory", "#f2b84b", "Raspberry Pi bereit", "Service-Datei und Installationsskript helfen beim dauerhaften Betrieb auf kleiner Hardware."),
            ("verified_user", "#e25563", "Kontrollierter Zugriff", "Blockierte Namen und eigene Nachrichten koennen ueber Einstellungen gesteuert werden."),
            ("public", "#374151", "Open Source", "Der Code kann geprueft, angepasst und ueber GitHub heruntergeladen werden."),
        ],
        "install_title": "Vom Download bis zum Dauerbetrieb",
        "install_copy": (
            "Das Projekt bleibt bewusst schlank: Python-Umgebung erstellen, Abhaengigkeiten installieren, "
            "Konfiguration anpassen und den Bot starten."
        ),
        "install_box_title": "Start in wenigen Befehlen",
        "github_open": "Auf GitHub oeffnen",
        "chart_title": "Beispielhafte Entlastung pro Woche",
        "chart_copy": "Weniger Wiederholungen, schnellere Antworten und klarere KA-Informationen.",
        "chart_bar": "Manuell beantwortete Fragen",
        "chart_line": "Mit WhatsApp Manager",
        "chart_days": ["Mo", "Di", "Mi", "Do", "Fr"],
        "architecture_title": "Architektur auf einen Blick",
        "architecture_copy": (
            "Die App trennt Konfiguration, WhatsApp-Web-Automation und einfache Textdateien. "
            "Dadurch laesst sie sich leicht verstehen, deployen und erweitern."
        ),
        "workflow_title": "Ablauf im Betrieb",
        "workflow_copy": "Der Service bleibt einfach: lesen, pruefen, aktualisieren, antworten.",
        "workflow_steps": [
            ("login", "WhatsApp Web", "QR-Code einmalig scannen"),
            ("groups", "Gruppe oeffnen", "Zielgruppe aus config.ini"),
            ("search", "Befehl erkennen", "/KA, /addKA oder /delKA"),
            ("edit_note", "Dateien pflegen", "Antwort und KA-Liste"),
            ("send", "Antwort senden", "Direkt in den Chat"),
        ],
        "system_title": "Systembausteine",
        "system_copy": "Eine kompakte Struktur fuer nachvollziehbare Automatisierung.",
        "system_parts": ["Selenium Bot", "config.ini", "KA-Dateien", "WhatsApp Web", "systemd"],
        "footer": "WhatsApp Manager ist ein Open-Source-Projekt von xinyulyuonline.",
    },
}

current_language = "en"


def tr() -> dict:
    return LANGUAGES[current_language]


def switch_language(value: str) -> None:
    global current_language
    current_language = value
    content.refresh()


def add_styles() -> None:
    ui.add_head_html(
        """
        <style>
        :root {
            --ink: #17202a;
            --muted: #5e6b78;
            --line: #d8e0e8;
            --paper: #f6f8fb;
            --green: #1fa855;
            --teal: #087f8c;
        }

        body {
            background: var(--paper);
            color: var(--ink);
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            letter-spacing: 0;
        }

        .page {
            width: 100%;
            min-height: 100vh;
            background:
                linear-gradient(180deg, rgba(255, 255, 255, 0.94), rgba(246, 248, 251, 0.96)),
                radial-gradient(circle at 16% 18%, rgba(31, 168, 85, 0.12), transparent 34%),
                radial-gradient(circle at 82% 10%, rgba(37, 99, 235, 0.10), transparent 28%);
        }

        .wrap {
            width: min(1180px, calc(100vw - 32px));
            margin: 0 auto;
        }

        .nav {
            min-height: 72px;
            border-bottom: 1px solid rgba(216, 224, 232, 0.78);
            backdrop-filter: blur(14px);
        }

        .brand-mark {
            width: 42px;
            height: 42px;
            border-radius: 8px;
            display: grid;
            place-items: center;
            color: white;
            background: linear-gradient(135deg, var(--green), var(--teal));
            box-shadow: 0 14px 32px rgba(31, 168, 85, 0.22);
        }

        .language-switch {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: white;
            padding: 4px;
        }

        .language-switch .q-btn {
            border-radius: 6px !important;
            min-height: 38px;
            font-weight: 760;
        }

        .hero {
            min-height: calc(100vh - 72px);
            padding: clamp(42px, 7vw, 82px) 0 34px;
            display: grid;
            align-items: center;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: minmax(0, 1.04fr) minmax(360px, 0.96fr);
            gap: clamp(28px, 5vw, 62px);
            align-items: center;
        }

        .eyebrow {
            width: fit-content;
            border: 1px solid rgba(31, 168, 85, 0.22);
            background: rgba(31, 168, 85, 0.08);
            color: #146c3a;
            border-radius: 999px;
            padding: 8px 12px;
            font-size: 13px;
            font-weight: 720;
        }

        .hero-title {
            font-size: clamp(42px, 7vw, 82px);
            line-height: 0.94;
            font-weight: 860;
            letter-spacing: 0;
            margin: 18px 0;
        }

        .hero-copy {
            max-width: 720px;
            color: var(--muted);
            font-size: clamp(17px, 2vw, 21px);
            line-height: 1.7;
        }

        .cta-row {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 30px;
        }

        .primary-btn,
        .secondary-btn {
            border-radius: 8px !important;
            min-height: 48px;
            padding: 0 18px !important;
            font-weight: 760 !important;
            box-shadow: none !important;
        }

        .primary-btn {
            background: var(--ink) !important;
            color: white !important;
        }

        .secondary-btn {
            border: 1px solid var(--line) !important;
            background: white !important;
            color: var(--ink) !important;
        }

        .mockup {
            border: 1px solid rgba(23, 32, 42, 0.12);
            border-radius: 8px;
            overflow: hidden;
            background: #f8fafc;
            box-shadow: 0 28px 80px rgba(23, 32, 42, 0.12);
        }

        .mockup-top {
            height: 46px;
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 0 15px;
            border-bottom: 1px solid var(--line);
            background: white;
        }

        .dot {
            width: 10px;
            height: 10px;
            border-radius: 99px;
            display: inline-block;
        }

        .screen {
            display: grid;
            grid-template-columns: 38% 62%;
            min-height: 440px;
        }

        .sidebar {
            border-right: 1px solid var(--line);
            background: #ffffff;
            padding: 16px;
        }

        .chat-list-item {
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 10px;
            background: #f1f5f9;
        }

        .chat-list-item.active {
            background: rgba(31, 168, 85, 0.12);
            border: 1px solid rgba(31, 168, 85, 0.24);
        }

        .chat {
            background:
                linear-gradient(45deg, rgba(31, 168, 85, 0.07) 25%, transparent 25%),
                linear-gradient(-45deg, rgba(37, 99, 235, 0.05) 25%, transparent 25%),
                #eef4f0;
            background-size: 34px 34px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .bubble {
            max-width: 82%;
            border-radius: 8px;
            padding: 11px 13px;
            line-height: 1.45;
            font-size: 14px;
            box-shadow: 0 4px 12px rgba(23, 32, 42, 0.08);
            white-space: pre-line;
        }

        .bubble.in {
            background: white;
            align-self: flex-start;
        }

        .bubble.out {
            background: #d9fdd3;
            align-self: flex-end;
        }

        .section {
            padding: clamp(54px, 7vw, 88px) 0;
            border-top: 1px solid rgba(216, 224, 232, 0.76);
        }

        .section-title {
            font-size: clamp(30px, 4vw, 48px);
            line-height: 1.08;
            font-weight: 830;
            margin: 0;
        }

        .section-copy {
            color: var(--muted);
            font-size: 17px;
            line-height: 1.65;
            max-width: 760px;
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 14px;
            margin-top: 30px;
        }

        .metric,
        .feature,
        .install-box,
        .diagram-box {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.88);
            box-shadow: 0 16px 44px rgba(23, 32, 42, 0.06);
        }

        .metric {
            padding: 20px;
        }

        .metric-number {
            font-size: 34px;
            font-weight: 840;
        }

        .metric-label {
            color: var(--muted);
            margin-top: 4px;
            line-height: 1.45;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
            margin-top: 34px;
        }

        .feature {
            padding: 22px;
        }

        .feature-icon {
            width: 42px;
            height: 42px;
            border-radius: 8px;
            display: grid;
            place-items: center;
            margin-bottom: 16px;
            color: white;
        }

        .feature-title {
            font-size: 18px;
            font-weight: 790;
            margin-bottom: 8px;
        }

        .feature-text {
            color: var(--muted);
            line-height: 1.6;
        }

        .split {
            display: grid;
            grid-template-columns: minmax(0, 0.92fr) minmax(360px, 1.08fr);
            gap: 24px;
            align-items: stretch;
            margin-top: 34px;
        }

        .install-box,
        .diagram-box {
            padding: 24px;
            overflow: hidden;
        }

        .code {
            border-radius: 8px;
            background: #111827;
            color: #e5e7eb;
            padding: 18px;
            font-family: "Cascadia Code", "SFMono-Regular", Consolas, monospace;
            font-size: 14px;
            line-height: 1.65;
            white-space: pre-wrap;
            overflow-wrap: anywhere;
        }

        .flow {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 10px;
            margin-top: 28px;
        }

        .step {
            min-height: 116px;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 14px;
            background: white;
        }

        .step strong {
            display: block;
            margin: 9px 0 4px;
        }

        .step span {
            color: var(--muted);
            font-size: 13px;
            line-height: 1.5;
        }

        .chart-holder {
            height: 390px;
            min-height: 390px;
        }

        .footer {
            padding: 34px 0 44px;
            color: var(--muted);
            border-top: 1px solid rgba(216, 224, 232, 0.76);
        }

        @media (max-width: 940px) {
            .hero {
                min-height: auto;
            }

            .hero-grid,
            .split {
                grid-template-columns: 1fr;
            }

            .screen {
                grid-template-columns: 1fr;
            }

            .sidebar {
                display: none;
            }

            .metric-grid,
            .feature-grid,
            .flow {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 700px) {
            .nav-row {
                flex-wrap: wrap;
                padding: 12px 0;
            }
        }

        @media (max-width: 620px) {
            .wrap {
                width: min(100vw - 22px, 1180px);
            }

            .metric-grid,
            .feature-grid,
            .flow {
                grid-template-columns: 1fr;
            }

            .hero-title {
                font-size: 42px;
            }

            .mockup {
                display: none;
            }
        }
        </style>
        """
    )


def icon_box(name: str, color: str) -> None:
    with ui.element("div").classes("feature-icon").style(f"background: {color};"):
        ui.icon(name).classes("text-white").props("size=24px")


def build_nav(text: dict) -> None:
    with ui.element("div").classes("nav"):
        with ui.element("div").classes("wrap"):
            with ui.row().classes("nav-row w-full items-center justify-between no-wrap").style("min-height: 72px; gap: 14px;"):
                with ui.row().classes("items-center no-wrap").style("gap: 12px;"):
                    with ui.element("div").classes("brand-mark"):
                        ui.icon("forum").props("size=24px")
                    with ui.column().classes("gap-0"):
                        ui.label(BRAND).classes("text-weight-bold text-lg")
                        ui.label(text["nav_subtitle"]).classes("text-xs text-grey-7")
                with ui.row().classes("items-center no-wrap").style("gap: 10px;"):
                    ui.label(text["language"]).classes("text-sm text-grey-7")
                    ui.toggle({"en": "EN", "de": "DE"}, value=current_language, on_change=lambda e: switch_language(e.value)).classes(
                        "language-switch"
                    ).props("unelevated toggle-color=primary")
                    ui.button(
                        text["github"],
                        icon="open_in_new",
                        on_click=lambda: ui.navigate.to(GITHUB_URL, new_tab=True),
                    ).classes("secondary-btn")


def build_mockup(text: dict) -> None:
    with ui.element("div").classes("mockup"):
        with ui.element("div").classes("mockup-top"):
            ui.element("span").classes("dot").style("background:#e25563;")
            ui.element("span").classes("dot").style("background:#f2b84b;")
            ui.element("span").classes("dot").style("background:#1fa855;")
            ui.label("web.whatsapp.com").classes("text-grey-7 text-sm q-ml-sm")
        with ui.element("div").classes("screen"):
            with ui.element("div").classes("sidebar"):
                ui.label(text["mockup_chats"]).classes("text-weight-bold q-mb-md")
                for title, meta, active in text["mockup_items"]:
                    with ui.element("div").classes(f"chat-list-item {'active' if active else ''}"):
                        ui.label(title).classes("text-weight-bold")
                        ui.label(meta).classes("text-grey-7 text-sm")
            with ui.element("div").classes("chat"):
                for direction, message in text["mockup_messages"]:
                    with ui.element("div").classes(f"bubble {direction}"):
                        ui.label(message)


def build_hero(text: dict) -> None:
    with ui.element("section").classes("hero"):
        with ui.element("div").classes("wrap hero-grid"):
            with ui.column().classes("items-start"):
                ui.label(text["eyebrow"]).classes("eyebrow")
                ui.label(BRAND).classes("hero-title")
                ui.label(text["hero_copy"]).classes("hero-copy")
                with ui.element("div").classes("cta-row"):
                    ui.button(
                        text["download"],
                        icon="download",
                        on_click=lambda: ui.navigate.to(GITHUB_URL, new_tab=True),
                    ).classes("primary-btn")
                    ui.button(
                        text["repo"],
                        icon="code",
                        on_click=lambda: ui.navigate.to(GITHUB_URL, new_tab=True),
                    ).classes("secondary-btn")
            build_mockup(text)


def build_metrics(text: dict) -> None:
    with ui.element("section").classes("section"):
        with ui.element("div").classes("wrap"):
            ui.label(text["metrics_title"]).classes("section-title")
            ui.label(text["metrics_copy"]).classes("section-copy q-mt-md")
            with ui.element("div").classes("metric-grid"):
                for number, label in text["metrics"]:
                    with ui.element("div").classes("metric"):
                        ui.label(number).classes("metric-number")
                        ui.label(label).classes("metric-label")


def build_features(text: dict) -> None:
    with ui.element("section").classes("section"):
        with ui.element("div").classes("wrap"):
            ui.label(text["features_title"]).classes("section-title")
            with ui.element("div").classes("feature-grid"):
                for icon, color, title, body in text["features"]:
                    with ui.element("div").classes("feature"):
                        icon_box(icon, color)
                        ui.label(title).classes("feature-title")
                        ui.label(body).classes("feature-text")


def build_chart(text: dict) -> None:
    options = {
        "backgroundColor": "transparent",
        "tooltip": {"trigger": "axis"},
        "legend": {"top": 0, "textStyle": {"color": "#5e6b78"}},
        "grid": {"left": 42, "right": 20, "bottom": 36, "top": 56},
        "xAxis": {
            "type": "category",
            "data": text["chart_days"],
            "axisLine": {"lineStyle": {"color": "#d8e0e8"}},
            "axisLabel": {"color": "#5e6b78"},
        },
        "yAxis": {
            "type": "value",
            "axisLabel": {"color": "#5e6b78"},
            "splitLine": {"lineStyle": {"color": "#e7edf3"}},
        },
        "series": [
            {
                "name": text["chart_bar"],
                "type": "bar",
                "data": [18, 21, 16, 23, 19],
                "itemStyle": {"color": "#d8e0e8", "borderRadius": [4, 4, 0, 0]},
            },
            {
                "name": text["chart_line"],
                "type": "line",
                "smooth": True,
                "data": [5, 4, 3, 4, 2],
                "symbolSize": 9,
                "lineStyle": {"width": 4, "color": "#1fa855"},
                "itemStyle": {"color": "#1fa855"},
                "areaStyle": {"color": "rgba(31, 168, 85, 0.12)"},
            },
        ],
    }
    with ui.element("div").classes("diagram-box"):
        ui.label(text["chart_title"]).classes("text-xl text-weight-bold")
        ui.label(text["chart_copy"]).classes("text-grey-7 q-mt-xs q-mb-md")
        ui.echart(options).classes("w-full chart-holder")


def build_workflow(text: dict) -> None:
    with ui.element("div").classes("diagram-box"):
        ui.label(text["workflow_title"]).classes("text-xl text-weight-bold")
        ui.label(text["workflow_copy"]).classes("text-grey-7 q-mt-xs")
        with ui.element("div").classes("flow"):
            for icon, title, body in text["workflow_steps"]:
                with ui.element("div").classes("step"):
                    ui.icon(icon).classes("text-primary").props("size=26px")
                    ui.html(f"<strong>{title}</strong><span>{body}</span>")


def build_install(text: dict) -> None:
    with ui.element("section").classes("section"):
        with ui.element("div").classes("wrap"):
            ui.label(text["install_title"]).classes("section-title")
            ui.label(text["install_copy"]).classes("section-copy q-mt-md")
            with ui.element("div").classes("split"):
                with ui.element("div").classes("install-box"):
                    ui.label(text["install_box_title"]).classes("text-xl text-weight-bold q-mb-md")
                    ui.html(
                        """
                        <pre class="code">git clone https://github.com/xinyulyuonline/WhatsApp-Manager
cd WhatsApp-Manager
python -m venv .venv
pip install -r requirements.txt
python whatsapp_manager.py --config config.ini</pre>
                        """
                    )
                    ui.button(
                        text["github_open"],
                        icon="open_in_new",
                        on_click=lambda: ui.navigate.to(GITHUB_URL, new_tab=True),
                    ).classes("primary-btn q-mt-lg")
                build_chart(text)


def build_diagram_section(text: dict) -> None:
    with ui.element("section").classes("section"):
        with ui.element("div").classes("wrap"):
            ui.label(text["architecture_title"]).classes("section-title")
            ui.label(text["architecture_copy"]).classes("section-copy q-mt-md")
            with ui.element("div").classes("split"):
                build_workflow(text)
                with ui.element("div").classes("diagram-box"):
                    ui.label(text["system_title"]).classes("text-xl text-weight-bold")
                    ui.label(text["system_copy"]).classes("text-grey-7 q-mt-xs q-mb-lg")
                    ui.echart(
                        {
                            "tooltip": {"trigger": "item"},
                            "series": [
                                {
                                    "type": "pie",
                                    "radius": ["42%", "72%"],
                                    "avoidLabelOverlap": True,
                                    "label": {"color": "#17202a", "formatter": "{b}"},
                                    "data": [
                                        {"value": 34, "name": text["system_parts"][0], "itemStyle": {"color": "#1fa855"}},
                                        {"value": 22, "name": text["system_parts"][1], "itemStyle": {"color": "#2563eb"}},
                                        {"value": 18, "name": text["system_parts"][2], "itemStyle": {"color": "#f2b84b"}},
                                        {"value": 16, "name": text["system_parts"][3], "itemStyle": {"color": "#087f8c"}},
                                        {"value": 10, "name": text["system_parts"][4], "itemStyle": {"color": "#e25563"}},
                                    ],
                                }
                            ],
                        }
                    ).classes("w-full chart-holder")


def build_footer(text: dict) -> None:
    with ui.element("footer").classes("footer"):
        with ui.element("div").classes("wrap"):
            with ui.row().classes("items-center justify-between w-full"):
                ui.label(text["footer"])
                ui.link("github.com/xinyulyuonline/WhatsApp-Manager", GITHUB_URL).classes("text-primary")


@ui.refreshable
def content() -> None:
    text = tr()
    with ui.element("main").classes("page"):
        build_nav(text)
        build_hero(text)
        build_metrics(text)
        build_features(text)
        build_install(text)
        build_diagram_section(text)
        build_footer(text)


@ui.page("/")
def index() -> None:
    ui.page_title(BRAND)
    add_styles()
    content()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title=BRAND, reload=False, port=8080)
