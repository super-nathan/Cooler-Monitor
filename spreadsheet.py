#!/usr/bin/python
# This script is called by CRON to monitor the 
# Temperatures and Humidities in the Main Cooler.
# It can also be called by watchtemps or another
# program or utility


import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 18


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

Celsius = temperature

temperature = 9.0/5.0 * Celsius + 32

humidity = format(humidity, '.2f')
temperature = format(temperature, '.2f')


# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print(temperature)
    print(humidity)
else:
    print('Failed to get reading. Try again!')




# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('/etc/googleauth/client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Shady Cold Room Temps").sheet1

#add a row, I think
dict = {}
dict['date'] = time.strftime('%m/%d/%Y')
dict['time'] = time.strftime('%H:%M')
dict['temperature'] = temperature
dict['humidity'] = humidity


##Debug
#print dict

row = [time.strftime('%m/%d/%Y'), time.strftime('%H:%M'), temperature, humidity]
index = 2
sheet.insert_row(row, index)



file = open('/tmp/tempnow.txt', 'w')
file.write(temperature + "\n")
file.close()
