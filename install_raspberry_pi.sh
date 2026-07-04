#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVICE_NAME="whatsapp-manager.service"
SERVICE_TARGET="/etc/systemd/system/${SERVICE_NAME}"

echo "Installing system packages..."
sudo apt update
sudo apt install -y python3 python3-venv
if ! sudo apt install -y chromium-browser chromium-chromedriver; then
  sudo apt install -y chromium chromium-driver
fi

echo "Creating Python virtual environment..."
python3 -m venv "${PROJECT_DIR}/.venv"
"${PROJECT_DIR}/.venv/bin/python" -m pip install --upgrade pip
"${PROJECT_DIR}/.venv/bin/pip" install -r "${PROJECT_DIR}/requirements.txt"

echo "Checking configuration..."
"${PROJECT_DIR}/.venv/bin/python" "${PROJECT_DIR}/whatsapp_manager.py" --config "${PROJECT_DIR}/config.ini" --check-config

echo "Installing systemd service..."
sed \
  -e "s#WorkingDirectory=/home/pi/WhatsApp-Manager#WorkingDirectory=${PROJECT_DIR}#" \
  -e "s#ExecStart=/home/pi/WhatsApp-Manager/.venv/bin/python /home/pi/WhatsApp-Manager/whatsapp_manager.py --config /home/pi/WhatsApp-Manager/config.ini#ExecStart=${PROJECT_DIR}/.venv/bin/python ${PROJECT_DIR}/whatsapp_manager.py --config ${PROJECT_DIR}/config.ini#" \
  "${PROJECT_DIR}/whatsapp-manager.service.example" | sudo tee "${SERVICE_TARGET}" >/dev/null

sudo systemctl daemon-reload
sudo systemctl enable "${SERVICE_NAME}"

echo
echo "Installed. Start once manually first to scan the WhatsApp Web QR code:"
echo "  ${PROJECT_DIR}/.venv/bin/python ${PROJECT_DIR}/whatsapp_manager.py --config ${PROJECT_DIR}/config.ini"
echo
echo "After the QR login works, start the service:"
echo "  sudo systemctl start ${SERVICE_NAME}"
