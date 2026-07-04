from __future__ import annotations

import argparse
import configparser
import hashlib
import logging
import shutil
import time
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.remote.webelement import WebElement


LOGGER = logging.getLogger("whatsapp-manager")
BASE_DIR = Path(__file__).resolve().parent
MAX_SEEN_MESSAGES = 300
VISIBLE_MESSAGE_LIMIT = 25
RESTART_DELAY_SECONDS = 10
CHROME_CANDIDATES = ["chromium-browser", "chromium", "google-chrome", "chrome"]
DRIVER_CANDIDATES = ["chromedriver"]


@dataclass(frozen=True)
class Settings:
    group_name: str
    command: str
    add_command: str
    del_command: str
    response_file: Path
    ka_list_file: Path
    blocked_add_names: tuple[str, ...]
    poll_interval_seconds: float
    binary_location: str | None
    driver_path: str | None
    profile_directory: Path
    headless: bool
    include_own_messages: bool


class SeenMessages:
    def __init__(self, max_size: int = MAX_SEEN_MESSAGES) -> None:
        self.max_size = max_size
        self._keys: set[str] = set()
        self._order: deque[str] = deque()

    def add(self, key: str) -> None:
        if key in self._keys:
            return

        self._keys.add(key)
        self._order.append(key)

        while len(self._order) > self.max_size:
            old_key = self._order.popleft()
            self._keys.discard(old_key)

    def update(self, keys: list[str]) -> None:
        for key in keys:
            self.add(key)

    def __contains__(self, key: object) -> bool:
        return key in self._keys

    def __len__(self) -> int:
        return len(self._keys)


def load_settings(config_path: Path) -> Settings:
    config_path = config_path.resolve()
    if not config_path.exists():
        raise FileNotFoundError(f"Config file does not exist: {config_path}")

    parser = configparser.ConfigParser()
    parser.read(config_path, encoding="utf-8")

    whatsapp = parser["whatsapp"] if parser.has_section("whatsapp") else {}
    browser = parser["browser"] if parser.has_section("browser") else {}

    response_file = Path(whatsapp.get("response_file", "ka_response.txt"))
    ka_list_file = Path(whatsapp.get("ka_list_file", "ka_list.txt"))
    profile_directory = Path(browser.get("profile_directory", ".whatsapp-profile"))
    config_dir = config_path.parent
    blocked_add_names = tuple(
        name.strip()
        for name in whatsapp.get("blocked_add_names", "").split(",")
        if name.strip()
    )

    settings = Settings(
        group_name=whatsapp.get("group_name", "Gruppe 8a"),
        command=whatsapp.get("command", "/KA").strip(),
        add_command=whatsapp.get("add_command", "/addKA").strip(),
        del_command=whatsapp.get("del_command", "/delKA").strip(),
        response_file=response_file if response_file.is_absolute() else config_dir / response_file,
        ka_list_file=ka_list_file if ka_list_file.is_absolute() else config_dir / ka_list_file,
        blocked_add_names=blocked_add_names,
        poll_interval_seconds=float(whatsapp.get("poll_interval_seconds", "0.5")),
        binary_location=(browser.get("binary_location", "").strip() or None),
        driver_path=(browser.get("driver_path", "").strip() or None),
        profile_directory=profile_directory
        if profile_directory.is_absolute()
        else config_dir / profile_directory,
        headless=browser.get("headless", "false").strip().lower() in {"1", "true", "yes", "on"},
        include_own_messages=browser.get("include_own_messages", "false").strip().lower()
        in {"1", "true", "yes", "on"},
    )

    validate_settings(settings)
    return settings


def validate_settings(settings: Settings) -> None:
    if not settings.group_name.strip():
        raise ValueError("Group name must not be empty.")
    if not settings.command:
        raise ValueError("Command must not be empty.")
    if not settings.add_command:
        raise ValueError("Add command must not be empty.")
    if not settings.del_command:
        raise ValueError("Delete command must not be empty.")
    if settings.poll_interval_seconds <= 0:
        raise ValueError("Poll interval must be greater than 0.")
    if not settings.response_file.exists():
        raise FileNotFoundError(f"Response file does not exist: {settings.response_file}")


def build_driver(settings: Settings) -> "WebDriver":
    from selenium import webdriver
    from selenium.webdriver import ChromeOptions
    from selenium.webdriver.chrome.service import Service

    settings.profile_directory.mkdir(parents=True, exist_ok=True)

    options = ChromeOptions()
    options.add_argument(f"--user-data-dir={settings.profile_directory}")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=0")
    options.add_argument("--window-size=1280,900")

    if settings.binary_location:
        options.binary_location = settings.binary_location
    if settings.headless:
        options.add_argument("--headless")

    service = Service(executable_path=settings.driver_path) if settings.driver_path else Service()
    return webdriver.Chrome(service=service, options=options)


def first_visible(driver: "WebDriver", selectors: list[str], timeout: int = 30) -> "WebElement":
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    wait = WebDriverWait(driver, timeout)
    last_error: Exception | None = None

    for selector in selectors:
        try:
            return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except TimeoutException as exc:
            last_error = exc

    raise TimeoutException(f"None of these selectors became visible: {selectors}") from last_error


def open_group(driver: "WebDriver", group_name: str) -> None:
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    driver.get("https://web.whatsapp.com/")
    LOGGER.info("Waiting for WhatsApp Web. Scan the QR code if this is the first start.")
    wait = WebDriverWait(driver, 120)
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@id="pane-side"] | //div[@role="grid"] | //canvas[@aria-label="Scan this QR code to link a device!"]',
            )
        )
    )
    LOGGER.info("WhatsApp Web is loaded. Looking for group: %s", group_name)

    try:
        visible_chat = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[@title={xpath_literal(group_name)}]"))
        )
        visible_chat.click()
        LOGGER.info("Opened group from chat list: %s", group_name)
        return
    except Exception:
        LOGGER.info("Group is not visible in chat list. Using search.")

    search_box = first_clickable_xpath(
        driver,
        [
            '//div[@contenteditable="true"][@role="textbox"][@aria-label="Search input textbox"]',
            '//div[@contenteditable="true"][@role="textbox"][contains(@aria-label, "Search")]',
            '//div[@contenteditable="true"][@role="textbox"][contains(@aria-label, "Suchen")]',
            '//div[@contenteditable="true"][@data-tab="3"]',
            '//div[@contenteditable="true"][@role="textbox"]',
        ],
        timeout=30,
    )
    search_box.click()
    search_box.send_keys(Keys.CONTROL, "a")
    search_box.send_keys(Keys.BACKSPACE)
    search_box.send_keys(group_name)
    LOGGER.info("Searching for group: %s", group_name)

    chat = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@title={xpath_literal(group_name)}]")))
    chat.click()
    LOGGER.info("Opened group: %s", group_name)


def first_clickable_xpath(driver: "WebDriver", xpaths: list[str], timeout: int = 30) -> "WebElement":
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    wait = WebDriverWait(driver, timeout)
    last_error: Exception | None = None

    for xpath in xpaths:
        try:
            return wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException as exc:
            last_error = exc

    raise TimeoutException(f"None of these XPaths became clickable: {xpaths}") from last_error


def xpath_literal(value: str) -> str:
    if '"' not in value:
        return f'"{value}"'
    if "'" not in value:
        return f"'{value}'"

    parts = value.split('"')
    return "concat(" + ', \'"\', '.join(f'"{part}"' for part in parts) + ")"


def message_key(element: "WebElement") -> str:
    data_id = element.get_attribute("data-id")
    if data_id:
        return data_id

    fingerprint = "|".join(
        [
            element.get_attribute("data-pre-plain-text") or "",
            element.text or "",
            str(element.location),
        ]
    )
    return hashlib.sha1(fingerprint.encode("utf-8")).hexdigest()


def message_sender(element: "WebElement") -> str:
    pre_plain_text = safe_attribute(element, "data-pre-plain-text")
    if "] " in pre_plain_text and pre_plain_text.endswith(": "):
        return pre_plain_text.split("] ", 1)[1][:-2].strip()
    if "] " in pre_plain_text and ":" in pre_plain_text:
        sender_part = pre_plain_text.split("] ", 1)[1]
        return sender_part.rsplit(":", 1)[0].strip()
    return ""


def safe_attribute(element: "WebElement", name: str) -> str:
    try:
        return element.get_attribute(name) or ""
    except Exception:
        return ""


def message_text(element: "WebElement") -> str:
    from selenium.webdriver.common.by import By

    selectors = [
        "span.selectable-text.copyable-text",
        "span.selectable-text",
        "div.copyable-text span[dir]",
        "span[dir]",
    ]

    for selector in selectors:
        try:
            parts = [part.text for part in element.find_elements(By.CSS_SELECTOR, selector) if part.text]
        except Exception:
            return ""
        text = "\n".join(parts).strip()
        if text:
            return text

    try:
        return (element.text or "").strip()
    except Exception:
        return ""


def is_own_message(element: "WebElement") -> bool:
    classes = safe_attribute(element, "class")
    data_id = safe_attribute(element, "data-id")
    if "message-out" in classes or data_id.startswith("true_"):
        return True

    try:
        return bool(
            element.parent.execute_script(
                "return Boolean(arguments[0].closest('.message-out'));",
                element,
            )
        )
    except Exception:
        return False


def read_messages(
    driver: "WebDriver",
    include_own_messages: bool = False,
    allowed_own_prefixes: tuple[str, ...] = (),
) -> list[tuple[str, str, str, bool]]:
    from selenium.webdriver.common.by import By

    selector = "div[data-id], div.message-in, div.message-out"
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    messages: list[tuple[str, str, str, bool]] = []

    for element in elements[-VISIBLE_MESSAGE_LIMIT:]:
        try:
            own_message = is_own_message(element)
            text = message_text(element)
            stripped_text = text.strip()
            if not stripped_text:
                continue

            own_command_allowed = any(command_argument(stripped_text, prefix) is not None for prefix in allowed_own_prefixes)
            if own_message and not include_own_messages and not own_command_allowed:
                continue

            messages.append((message_key(element), stripped_text, message_sender(element), own_message))
        except Exception:
            continue

    return messages


def should_respond(message: str, command: str) -> bool:
    return message.strip().casefold() == command.strip().casefold()


def command_argument(message: str, command: str) -> str | None:
    text = message.strip()
    command = command.strip()
    if not text.casefold().startswith(command.casefold()):
        return None

    rest = text[len(command) :]
    if rest and not rest[0].isspace():
        return None
    return rest.strip()


def read_response(settings: Settings) -> str:
    response = settings.response_file.read_text(encoding="utf-8").strip()
    ka_entries = read_ka_entries(settings)
    combined = "\n".join(part for part in [response, ka_entries] if part).strip()
    if not combined:
        raise ValueError(f"Response file is empty: {settings.response_file}")
    return combined


def read_ka_entries(settings: Settings) -> str:
    return "\n".join(read_ka_lines(settings)).strip()


def read_ka_lines(settings: Settings) -> list[str]:
    if not settings.ka_list_file.exists():
        return []
    return [
        line.strip()
        for line in settings.ka_list_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def append_ka_entry(settings: Settings, entry: str) -> None:
    settings.ka_list_file.parent.mkdir(parents=True, exist_ok=True)
    with settings.ka_list_file.open("a", encoding="utf-8") as file:
        if settings.ka_list_file.exists() and settings.ka_list_file.stat().st_size > 0:
            file.write("\n")
        file.write(entry.strip())


def delete_ka_entry(settings: Settings, query: str) -> tuple[str, list[str]]:
    query = query.strip()
    if not query:
        return ("empty", [])

    entries = read_ka_lines(settings)
    matches = [entry for entry in entries if query.casefold() in entry.casefold()]

    if not matches:
        return ("none", [])
    if len(matches) > 1:
        return ("multiple", matches)

    entry_to_delete = matches[0]
    remaining = [entry for entry in entries if entry != entry_to_delete]
    settings.ka_list_file.write_text(
        ("\n".join(remaining) + "\n") if remaining else "",
        encoding="utf-8",
    )
    return ("deleted", [entry_to_delete])


def is_blocked_sender(sender: str, settings: Settings) -> bool:
    return any(sender.casefold() == blocked.casefold() for blocked in settings.blocked_add_names)


def process_new_messages(
    messages: list[tuple[str, str, str, bool]],
    seen: SeenMessages,
    settings: Settings,
    send: Callable[[str], None],
) -> int:
    responses_sent = 0

    for key, text, sender, own_message in messages:
        if key in seen:
            continue

        seen.add(key)
        if should_respond(text, settings.command):
            LOGGER.info("Command received: %s", settings.command)
            send(read_response(settings))
            responses_sent += 1
        else:
            add_entry = command_argument(text, settings.add_command)
            del_query = command_argument(text, settings.del_command)

            if add_entry is not None:
                if not own_message and is_blocked_sender(sender, settings):
                    LOGGER.info("Blocked add command from: %s", sender or "unknown")
                    send("Du bist nicht berechtigt, diesen Befehl zu benutzen.")
                    responses_sent += 1
                elif not add_entry:
                    send(f"Bitte schreibe nach {settings.add_command} noch eine Nachricht.")
                    responses_sent += 1
                else:
                    append_ka_entry(settings, add_entry)
                    LOGGER.info("Added KA entry from %s: %s", sender, add_entry)
                    send(f"KA wurde hinzugefuegt: {add_entry}")
                    responses_sent += 1
            elif del_query is not None:
                if not own_message and is_blocked_sender(sender, settings):
                    LOGGER.info("Blocked delete command from: %s", sender or "unknown")
                    send("Du bist nicht berechtigt, diesen Befehl zu benutzen.")
                    responses_sent += 1
                else:
                    status, matches = delete_ka_entry(settings, del_query)
                    if status == "empty":
                        send(f"Bitte schreibe nach {settings.del_command} noch einen Suchtext.")
                    elif status == "none":
                        send(f"Kein KA-Eintrag gefunden fuer: {del_query}")
                    elif status == "multiple":
                        send("Es gibt mehrere Moeglichkeiten:\n" + "\n".join(matches))
                    else:
                        send(f"KA wurde geloescht: {matches[0]}")
                    responses_sent += 1

    return responses_sent


def resolve_executable(configured_path: str | None, candidates: list[str]) -> str | None:
    if configured_path:
        path = Path(configured_path)
        return str(path) if path.exists() else None

    for candidate in candidates:
        found = shutil.which(candidate)
        if found:
            return found
    return None


def doctor_lines(settings: Settings) -> list[str]:
    response = read_response(settings)
    chrome = resolve_executable(settings.binary_location, CHROME_CANDIDATES)
    driver = resolve_executable(settings.driver_path, DRIVER_CANDIDATES)

    lines = [
        "Config: OK",
        f"Group: {settings.group_name}",
        f"Command: {settings.command}",
        f"Poll interval: {settings.poll_interval_seconds}s",
        f"Response file: {settings.response_file} ({len(response)} chars)",
        f"Profile directory: {settings.profile_directory}",
        f"Chrome/Chromium: {chrome or 'not found automatically'}",
        f"Chromedriver: {driver or 'not found automatically'}",
        f"Headless: {settings.headless}",
        f"Include own messages: {settings.include_own_messages}",
    ]

    if not chrome and not settings.binary_location:
        lines.append("Hint: set browser.binary_location in config.ini if Selenium cannot find Chromium.")
    if not driver and not settings.driver_path:
        lines.append("Hint: set browser.driver_path in config.ini if Selenium cannot find Chromedriver.")

    return lines


def simulate_message(message: str, settings: Settings) -> str | None:
    sent: list[str] = []
    process_new_messages([("simulation-message", message, "Simulation", True)], SeenMessages(), settings, sent.append)
    return sent[0] if sent else None


def send_message(driver: "WebDriver", text: str) -> None:
    from selenium.webdriver.common.keys import Keys

    box = first_visible(
        driver,
        [
            'footer div[contenteditable="true"][role="textbox"]',
            'footer div[contenteditable="true"][data-tab="10"]',
        ],
        timeout=15,
    )
    box.click()

    lines = text.splitlines() or [text]
    for index, line in enumerate(lines):
        if index:
            box.send_keys(Keys.SHIFT, Keys.ENTER)
        box.send_keys(line)
    box.send_keys(Keys.ENTER)


def run_session(settings: Settings) -> None:
    driver = build_driver(settings)
    seen = SeenMessages()

    try:
        open_group(driver, settings.group_name)
        initial_messages = read_messages(
            driver,
            settings.include_own_messages,
            allowed_own_prefixes=(settings.add_command, settings.del_command),
        )
        seen.update([key for key, _, _, _ in initial_messages])
        LOGGER.info("Initial messages loaded: %s", len(initial_messages))
        LOGGER.info("Bot is running. Watching for %r every %.1fs.", settings.command, settings.poll_interval_seconds)

        loop_count = 0
        while True:
            messages = read_messages(
                driver,
                settings.include_own_messages,
                allowed_own_prefixes=(settings.add_command, settings.del_command),
            )
            sent = process_new_messages(
                messages,
                seen,
                settings,
                lambda text: send_message(driver, text),
            )
            if sent:
                LOGGER.info("Sent %s response(s).", sent)
            loop_count += 1
            if loop_count % 20 == 0:
                LOGGER.info("Still running. Messages visible: %s. Seen cache: %s.", len(messages), len(seen))
            time.sleep(settings.poll_interval_seconds)
    finally:
        driver.quit()


def run_bot(settings: Settings) -> None:
    while True:
        try:
            run_session(settings)
        except KeyboardInterrupt:
            LOGGER.info("Stopping bot.")
            raise
        except Exception:
            LOGGER.exception("Bot session crashed. Restarting in %s seconds.", RESTART_DELAY_SECONDS)
            time.sleep(RESTART_DELAY_SECONDS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Watch a WhatsApp group and answer a configured command.")
    parser.add_argument("--config", default="config.ini", help="Path to the INI configuration file.")
    parser.add_argument("--check-config", action="store_true", help="Validate configuration and exit.")
    parser.add_argument("--doctor", action="store_true", help="Print runtime diagnostics without opening WhatsApp.")
    parser.add_argument("--simulate-message", help="Process one fake incoming message without opening WhatsApp.")
    parser.add_argument("--verbose", action="store_true", help="Show debug logging.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = BASE_DIR / config_path

    settings = load_settings(config_path)
    read_response(settings)
    if args.doctor:
        for line in doctor_lines(settings):
            print(line)
        return

    if args.simulate_message is not None:
        response = simulate_message(args.simulate_message, settings)
        if response is None:
            print("No response would be sent.")
        else:
            print(response)
        return

    if args.check_config:
        LOGGER.info("Configuration is valid.")
        return

    run_bot(settings)


if __name__ == "__main__":
    main()
