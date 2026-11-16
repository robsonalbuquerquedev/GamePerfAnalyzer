import os
import subprocess


ADB_PATH = os.getenv("ADB_PATH", "adb")


def list_devices():
    try:
        result = subprocess.run(
            [ADB_PATH, "devices", "-l"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or "ADB command failed")

        devices = []

        for line in result.stdout.splitlines()[1:]:
            parts = line.split()

            if len(parts) < 2 or line.startswith("*"):
                continue

            serial = parts[0]
            state = parts[1]

            attributes = {}

            for item in parts[2:]:
                if ":" in item:
                    key, value = item.split(":", 1)
                    attributes[key] = value

            devices.append({
                "serial": serial,
                "state": state,
                "authorized": state == "device",
                "model": attributes.get("model"),
                "product": attributes.get("product"),
                "device": attributes.get("device")
            })

        return devices

    except FileNotFoundError:
        raise RuntimeError("ADB executable was not found")

    except subprocess.TimeoutExpired:
        raise RuntimeError("ADB command timed out")
    
def get_connected_device():
    devices = list_devices()

    if not devices:
        raise RuntimeError("No Android device connected")

    if len(devices) > 1:
        raise RuntimeError(
            "Multiple devices detected. Connect only one device."
        )

    device = devices[0]

    if device["state"] != "device":
        raise RuntimeError(
            f"Device {device['serial']} is not ready. "
            f"Current state: {device['state']}"
        )

    return device