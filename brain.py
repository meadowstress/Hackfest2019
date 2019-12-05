import receiver
import relay_communicator

def run():
    print("Hi, I am the brain")
    count = 0
    max_count = 10;
    while count < max_count:
        b = receiver.check_input_dummy()
        if b:
            relay_communicator.switch_on_relay()
        count = count + 1


if __name__ == '__main__':
    exit(run())