def switch_on_relay():
    print("Turn on the relay!")

def check_input():
    print("Check input")
    return True

def run():
    print("Hi, I am the brain")
    count = 0
    max_count = 10;
    while count < max_count:
        b = check_input()
        if b:
            switch_on_relay()
        count = count + 1