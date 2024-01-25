"""
This code is Belogs to SME Dehradun Firm. For any query, mail us at schematicslab@gmail.com 
"""

import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
import time

#BLYNK_AUTH_TOKEN = 'hWRSpWldCWv-ha5aqmasPkbObCIvxNGX'

device1 = 22
device2 = 23
GPIO.setmode(GPIO.BCM)


GPIO.setup(device1, GPIO.OUT)
GPIO.setup(device2, GPIO.OUT)

GPIO.output(device1, GPIO.LOW)
GPIO.output(device2, GPIO.LOW)
# Initialize Blynk
blynk = BlynkLib.Blynk('80Uq7fRkN62oxQOFw5KOoHB197ZefM3k')

# Led control through V0 virtual pin
@blynk.on("V0")
def v0_write_handler(value):
#    global device_switch
    if int(value[0]) is not 0:
        GPIO.output(device1, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(device1, GPIO.LOW)
        print('open ')
    else:
        GPIO.output(device1, GPIO.LOW)
        print('not open')


# Led control through V1 virtual pin
@blynk.on("V1")
def v1_write_handler(value):
#    global device_switch
    if int(value[0]) is not 0:
        GPIO.output(device2, GPIO.HIGH)
        
        time.sleep(3)
        GPIO.output(device2, GPIO.LOW)
        
        print('close')
        
        
    else:
        GPIO.output(device2, GPIO.LOW)
        print('not close')



#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Alert: Hi! Raspberry Pi Connected to New Blynk2.0") 

while True:
    blynk.run()
