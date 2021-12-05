import sys
import asyncio
import platform
import time
import requests

from bleak import BleakClient

EVENTS = ["Dishwasher", "Oven", "Hairdryer"]

# you can change these to match your device or override them from the command line
CHARACTERISTIC_UUID = "00002a57-0000-1000-8000-00805f9b34fb"

ADDRESS = (
    "91:0C:EC:15:4A:FE"
)

def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    event_number = int.from_bytes(bytes=data,byteorder="little", signed=False)
    print("{0}: {1}".format(sender, event_number))
    r = requests.post(f"https://maker.ifttt.com/trigger/RPI_EVENT/with/key/czpWqSQT7vXx8EvUU5Qt-x", params={"value1":f"appliance_name ... {event_number}","value2":"duraiton","value3":"normal/avg/threshold"})


async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(60.0)
        await client.stop_notify(char_uuid)


if __name__ == "__main__":
    asyncio.run(
        main(
            sys.argv[1] if len(sys.argv) > 1 else ADDRESS,
            sys.argv[2] if len(sys.argv) > 2 else CHARACTERISTIC_UUID,
        )
    )