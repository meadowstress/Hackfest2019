import relay_communicator
import time
import receiver


def run():
    print("Hi, I am the simple brain")
    relay = relay_communicator.RelayCommunicator()
    received_signal = receiver.Receiver()

    while 1:
        #activation_request = received_signal.check_input_from_keyboard()
        activation_request = received_signal.check_engage_switch()
        print("Activation request = ", activation_request)
        relay.activate(activation_request)
        print("sleep")
        time.sleep(0.4)

    print("Exit Program!")


if __name__ == '__main__':
    exit(run())
