import RPi.GPIO as GPIO


class RelayCommunicator:

    def __init__(self):
        self.OUTPUT_PIN = 3  # GPIO2
        # to use Raspberry Pi board pin numbers
        GPIO.setmode(GPIO.BOARD)
        # Specify OUTPUT_PIN as output
        GPIO.setup(self.OUTPUT_PIN, GPIO.OUT)
        GPIO.output(self.OUTPUT_PIN, GPIO.HIGH)  # init pin state
        self.last_state = False

    def activate(self, activate):
        if self.signalChanged(activate):
            if activate:
                print("Turn on the relay!")
                # LOW (active)
                GPIO.output(self.OUTPUT_PIN, GPIO.LOW)
            else:
                print("Turn off the relay!")
                # HIGH (deactive)
                GPIO.output(self.OUTPUT_PIN, GPIO.HIGH)
        self.last_state = activate

    def __del__(self):
        print("Delete Relay communicator")
        GPIO.cleanup()

    def signalChanged(self, input):
        return(input != self.last_state)
