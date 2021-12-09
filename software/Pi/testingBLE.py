import sys
import asyncio
import platform
import time
import requests
from enum import Enum

from bleak import BleakClient

class event_type(Enum):
    open_close = 1
    continuous = 2

#threshold: Time before a notification (seconds).
#type: Whether we are recognizing an event (open/closing fridge) or a continous sound, like water running.
EVENT_INDEX = ["Blender","Boiling Water","Dishwasher",
            "Drying Machine","Fridge",
            "Hairdryer","Kettle","Microwave","Stovefan",
            "Washing Machine","Running Water"]
EVENTS = {  "Blender":{"threshold" : 5,"type":event_type.continuous},
            "Boiling Water":{"threshold" : 5,"type":event_type.continuous},
            "Dishwasher":{"threshold" : 5,"type":event_type.continuous},
            "Drying Machine":{"threshold" : 5,"type":event_type.continuous},
            "Fridge":{"threshold" : 5,"type":event_type.open_close},
            "Hairdryer":{"threshold" : 5,"type":event_type.continuous},
            "Kettle":{"threshold" : 5,"type":event_type.continuous},
            "Microwave":{"threshold" : 5,"type":event_type.continuous},
            "Stovefan":{"threshold" : 5,"type":event_type.continuous},
            "Washing Machine":{"threshold" : 5,"type":event_type.continuous},
            "Running Water":{"threshold" : 5,"type":event_type.continuous}
}

timeout = 10 #How long it takes before an appliance is "off"
# Must be greater than threshold for event based detection (like fridge open/close)

CURRENT_RUNNING = {} #Dictionary of currently running appliances and when they started.

# you can change these to match your device or override them from the command line
CHARACTERISTIC_UUID = "00002a57-0000-1000-8000-00805f9b34fb"

ADDRESS = (
    "91:0C:EC:15:4A:FE"
)

#Jackie address
ADDRESS = (
    "29:17:1d:93:48:e7"
)
def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    event_number = int.from_bytes(bytes=data,byteorder="little", signed=False)
    print("{0}: {1}".format(sender, event_number))
    event_name = EVENT_INDEX[event_number]
    current_event_type = EVENTS[event_name]["type"]
    current_time = time.time()
    if (not event_name in CURRENT_RUNNING): #Event hasn't been heard before
        CURRENT_RUNNING[event_name] = current_time
    if (event_name in CURRENT_RUNNING and current_time - CURRENT_RUNNING[event_name] > timeout): #It has been so long it is a new event at this point
        CURRENT_RUNNING[event_name] = current_time
    for event, start_time in list(CURRENT_RUNNING.items()):
        duration = current_time - start_time
        threshold =  EVENTS[event]["threshold"]
        if duration > threshold: #It has been on so long its time for a notification
            r = requests.post(f"https://maker.ifttt.com/trigger/RPI_EVENT/with/key/czpWqSQT7vXx8EvUU5Qt-x", params={"value1":event_name,"value2":duration,"value3":threshold})
            CURRENT_RUNNING.pop(event)
        elif duration > timeout and event_name != event: #The event hasn't been heard in a while and wasn't long enough to trigger an event.
            CURRENT_RUNNING.pop(event)



async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(600.0) #Runs for 10 minutes unless stopped
        await client.stop_notify(char_uuid)


if __name__ == "__main__":
    asyncio.run(main(ADDRESS,CHARACTERISTIC_UUID))
