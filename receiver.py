def check_input_dummy():
    print("Check input, return true")
    return True


def check_input_from_keyboard():
    activation_keys = ["yes", "y", "alarm",
                       "911", "cake", "fika", "lunch", "lellky"]
    print("Check input from keyboard")
    activation_request_string = input("Do you want to activate? ")
    print(activation_request_string)
    activation_request = activation_request_string in activation_keys
    return activation_request
