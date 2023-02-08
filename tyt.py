import asyncio
import bleak


async def scan(beacon):
    while True:
        scanned_devices = await bleak.BleakScanner.discover(1)
        for device in scanned_devices:
            if device.name == beacon:
                print(scanned_devices)
                return beacon


print(asyncio.run(scan("Cs_1")))
