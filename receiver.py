def check_input_dummy():
    print("Check input, return true")
    return True

def check_input_from_keyboard():
    print("Check input from keyboard")
    activation_request_string = input("Do you want to activate?")
    return activation_request_string.lower() == "yes"