from slack_alarm_bot import SlackAlarmBot
import relay_communicator
import atexit
import time


def run():
    print("Hi, I am the brain")

    #commented out below as it is blocking. Need to run asynch.
    #alarm_bot = SlackAlarmBot()

    count = 0
    max_count = 10
    relay = relay_communicator.RelayCommunicator()
    while count < max_count:
        activation_request = receiver.check_input_from_keyboard()
        print("Activation request = ", activation_request)
        #activation_request = arbitrate(activation_requests)
        relay.activate(activation_request)
        count = count + 1
        print("sleep")
        time.sleep(1)


if __name__ == '__main__':
    exit(run())
