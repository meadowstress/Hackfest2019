from slack_alarm_bot import SlackAlarmBot
import asyncio
import relay_communicator
import time
import receiver

async def do_work():
    count = 0
    max_count = 10
    relay = relay_communicator.RelayCommunicator()
    received_signal = receiver.Receiver()
    while count < max_count:
        activation_request = received_signal.check_input_from_keyboard()
        print("Activation request = ", activation_request)
        #activation_request = arbitrate(activation_requests)
        relay.activate(activation_request)
        count = count + 1
        print("sleep")
        time.sleep(1)

def run():
    print("Hi, I am the brain")

    alarm_bot = SlackAlarmBot()

    loop = asyncio.get_event_loop()
    loop.create_task(do_work())
    loop.create_task(alarm_bot.rtm_client.start())

    loop.run_forever()
    loop.close()


if __name__ == '__main__':
    exit(run())
