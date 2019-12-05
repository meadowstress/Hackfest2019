import relay_communicator
import time

rc = relay_communicator.RelayCommunicator()
rc.activate_relay(True)
time.sleep(5.0)
rc.activate_relay(False)