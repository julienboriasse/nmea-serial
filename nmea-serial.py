from datetime import datetime, timedelta, timezone
from nmeasim.models import GpsReceiver
import time
import serial
import keyboard
import random

# Function to get a random invalid NMEA prefix
def get_invalid_NMEA_prefix():
    return random.choice([b'GPGGA', b'GPGSA', b'GPGSV', b'GPGLL', b'GPVTG', b'GPZDA'])
        

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

correct_output = True

# Send the GPS data to the serial port
starting_time = time.time()

while True:
    if time.time() - starting_time > 1:
        # Update the date_time variable
        starting_time = time.time()
        gps.date_time += timedelta(seconds=1)

        # Get the GPS data
        if correct_output:
            gps_output = str(gps.get_output()[0]).encode('utf-8')
        else:
            gps_output = str(gps.get_output()[0]).encode('utf-8').replace(b'GPRMC', get_invalid_NMEA_prefix())

        print(gps_output.decode())
        ser.write(gps_output)
    
    # Check if I pressed correct output key - c
    if keyboard.is_pressed("c"):
        correct_output = not correct_output
        if correct_output:
            print("Correct output")
        else:  
            print("Incorrect output")
        time.sleep(0.5)

    # Check if I pressed escape key - q
    if keyboard.is_pressed("q"):
        # Key was pressed
        break
