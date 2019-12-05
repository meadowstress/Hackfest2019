import receiver

rc = receiver.Receiver()
activation_request = rc.check_input_from_keyboard()
if activation_request:
    print("yes")
else:
    print("no")
