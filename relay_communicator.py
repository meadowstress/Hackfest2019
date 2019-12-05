import RPi.GPIO as GPIO
import time

def activate_relay(activate):
    OUTPUT_PIN = 3  # GPIO2

    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)
    # Specify OUTPUT_PIN as output
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)
    if activate:
        print("Turn on the relay!")
        # LOW (active)
        GPIO.output(OUTPUT_PIN, GPIO.LOW)
    else:
        print("Turn off the relay!")
        # HIGH (deactive)
        GPIO.output(OUTPUT_PIN, GPIO.HIGH)

    GPIO.cleanup()


