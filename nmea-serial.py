from datetime import datetime, timedelta, timezone
from nmeasim.models import GpsReceiver
import time
import serial
import keyboard

# Listen to keys and quit script if I press escape key
def on_press(key):
    if key == keyboard.Key.esc:
        return False
        

# Serial device configuration
COM_PORT = 'COM20'  # COM port of the serial device
COM_SPEED = 115200  # COM speed of the serial device

# Open the serial port
ser = serial.Serial(COM_PORT, COM_SPEED, timeout=1)

# Variable date_time containing current date and time in Montreal timezone
date_time = datetime.now(timezone(timedelta(hours=-5)))

# Create a GPS receiver object
gps = GpsReceiver(
    date_time=date_time,
    output=('RMC',))

# Send the GPS data to the serial port
starting_time = time.time()

while True:
    if time.time() - starting_time > 1:
        # Update the date_time variable
        starting_time = time.time()
        gps.date_time += timedelta(seconds=1)

        # Get the GPS data
        gps_output = str(gps.get_output()).encode('utf-8')
        print(gps_output)
        ser.write(gps_output)

    # Check if I pressed escape key - q
    if keyboard.is_pressed("q"):
        # Key was pressed
        break
