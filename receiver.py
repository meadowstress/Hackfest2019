import RPi.GPIO as GPIO


class Receiver:

    def __init__(self):
        self.system_engaged = False
        self.PIN_ENGAGED = 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PIN_ENGAGED, GPIO.IN)

    def __del__(self):
        print("Delete Receiver")
        GPIO.cleanup()

    def check_input_dummy(self):
        print("Check input, return true")
        return True

    def check_input_from_keyboard(self):
        activation_keys = ["yes", "y", "alarm",
                           "911", "cake", "fika", "lunch", "lellky"]
        print("Check input from keyboard")
        activation_request_string = input("Do you want to activate? ")
        print(activation_request_string)
        activation_request = activation_request_string in activation_keys
        return activation_request

    def check_engage_switch(self):
        return(GPIO.input(self.PIN_ENGAGED) == GPIO.LOW)
