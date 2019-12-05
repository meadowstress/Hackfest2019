import receiver
import relay_communicator
import atexit


def run():
    print("Hi, I am the brain")
    count = 0
    max_count = 10
    relay = relay_communicator.RelayCommunicator()
    while count < max_count:
        activation_request = receiver.check_input_dummy()
        print("Activation request = ", activation_request)
        relay.activate(activation_request)
        count = count + 1


if __name__ == '__main__':
    exit(run())
