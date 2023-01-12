from datetime import datetime, timedelta, timezone
from nmeasim.models import GpsReceiver
import time
import serial

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
while True:
    # Wait for 1 second
    time.sleep(1)

    gps.date_time += timedelta(seconds=1)
    gps_output = str(gps.get_output()).encode('utf-8')
    print(gps_output)
    ser.write(gps_output)