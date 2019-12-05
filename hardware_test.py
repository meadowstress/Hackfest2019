#https://medium.com/@isma3il/install-python-3-6-or-3-7-and-pip-on-raspberry-pi-85e657aadb1e

print("Hallo Welt!")

import RPi.GPIO as GPIO
import time

OUTPUT_PIN = 3 # GPIO2

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# Specify OUTPUT_PIN as output
GPIO.setup(OUTPUT_PIN, GPIO.OUT)

# Initialize output pin with HIGH (deactive)
GPIO.output(OUTPUT_PIN, GPIO.HIGH)

# Let it blink
for i in range(5):
    GPIO.output(OUTPUT_PIN, GPIO.LOW)
    time.sleep(5.0)
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    time.sleep(1.0)

GPIO.cleanup()

