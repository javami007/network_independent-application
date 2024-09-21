import bleak  # For Bluetooth Low Energy
import pywifi  # For Wi-Fi Direct

# Bluetooth scanning and connection setup
async def setup_ble():
    devices = await bleak.BleakScanner.discover()
    for device in devices:
        print(f"Found Bluetooth device: {device}")

# Wi-Fi Direct connection setup
def setup_wifi_direct():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()  # Scan for Wi-Fi Direct devices
    print(f"Found Wi-Fi Direct devices: {iface.scan_results()}")

if __name__ == "__main__":
    # Initialize BLE and Wi-Fi Direct
    import asyncio
    asyncio.run(setup_ble())
    setup_wifi_direct()

