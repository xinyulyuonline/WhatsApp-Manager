# WhatsApp-Manager

Ein kleiner Python-Bot fuer WhatsApp Web. Er oeffnet die Gruppe `Gruppe 8a`, liest neue eingehende Nachrichten alle `0.5` Sekunden und sendet den Inhalt aus `ka_response.txt`, sobald jemand `/KA` schreibt.

## Installation

```bash
sudo apt update
sudo apt install -y python3 python3-venv chromium-browser chromium-chromedriver
# Falls diese Chromium-Pakete auf deinem Pi nicht existieren:
# sudo apt install -y chromium chromium-driver
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Oder auf dem Raspberry Pi automatisch vorbereiten:

```bash
bash install_raspberry_pi.sh
```

Auf Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Konfiguration

Passe bei Bedarf `config.ini` an:

```ini
[whatsapp]
group_name = Gruppe 8a
command = /KA
add_command = /addKA
del_command = /delKA
response_file = ka_response.txt
ka_list_file = ka_list.txt
poll_interval_seconds = 0.5
blocked_add_names = Max, Anna
```

Die feste Antwort steht in `ka_response.txt`. Neue KA-Eintraege durch `/addKA ...` werden in `ka_list.txt` gespeichert. Mit `/delKA Mathe` wird ein passender Eintrag geloescht; bei mehreren Treffern schickt der Bot die passenden Moeglichkeiten.

Auf manchen Raspberry-Pi-Installationen liegen Chromium und Chromedriver hier:

```ini
[browser]
binary_location = /usr/bin/chromium-browser
driver_path = /usr/bin/chromedriver
```

Wenn der Bot spaeter ohne sichtbaren Desktop per systemd laufen soll, scanne den QR-Code zuerst einmal mit `headless = false`. Danach kannst du in `config.ini` auf `headless = true` stellen.

## Start

Bot starten:

```bash
python whatsapp_manager.py --config config.ini
```

Beim ersten Start oeffnet sich WhatsApp Web. Scanne den QR-Code mit deinem Handy. Danach bleibt die Sitzung im Ordner `whatsapp-profile` gespeichert, damit der Bot auf dem Raspberry Pi nach einem Neustart wieder starten kann.

## Raspberry Pi dauerhaft laufen lassen

Kopiere die Vorlage:

```bash
sudo cp whatsapp-manager.service.example /etc/systemd/system/whatsapp-manager.service
```

Falls dein Projekt nicht unter `/home/pi/WhatsApp-Manager` liegt, passe `WorkingDirectory` und `ExecStart` in `/etc/systemd/system/whatsapp-manager.service` an.

Bei Raspberry Pi OS mit Desktop kannst du alternativ `headless = false` lassen. Dann braucht der Service Zugriff auf den laufenden Desktop, zum Beispiel mit `Environment=DISPLAY=:0` in der Service-Datei.

Dann aktivieren und starten:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now whatsapp-manager.service
```

Logs ansehen:

```bash
sudo journalctl -u whatsapp-manager.service -f
```

Hinweis: WhatsApp Web kann seine Oberflaeche aendern. Wenn der Bot ploetzlich keine Nachrichten mehr findet, muessen eventuell die Selenium-Selektoren in `whatsapp_manager.py` angepasst werden.
