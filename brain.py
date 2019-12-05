import receiver
import relay_communicator
import atexit
import RPi.GPIO as GPIO


def cleanup():
    GPIO.cleanup()


def run():
    print("Hi, I am the brain")
    count = 0
    max_count = 10
    relay = relay_communicator.RelayCommunicator()
    while count < max_count:
        relay.activate(receiver.check_input_dummy())
        count = count + 1
        atexit.register(cleanup)


if __name__ == '__main__':
    exit(run())
