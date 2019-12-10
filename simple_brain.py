import relay_communicator
import time
import receiver


def run():
    print("Hi, I am the stupid brain")
    count = 0
    max_count = 30
    relay = relay_communicator.RelayCommunicator()
    received_signal = receiver.Receiver()
    system_on = True
    while max_count:
        system_on = received_signal.check_system_on()
        #activation_request = received_signal.check_input_from_keyboard()
        activation_request = received_signal.check_engage_switch()
        print("Activation request = ", activation_request)
        relay.activate(activation_request)
        count = count + 1
        print("sleep")
        time.sleep(0.4)

    print("Exit Program!")


if __name__ == '__main__':
    exit(run())
