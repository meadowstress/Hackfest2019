from slack_alarm_bot import SlackAlarmBot
import asyncio
import relay_communicator
import time
import receiver


async def do_work():
    relay = relay_communicator.RelayCommunicator()
    received_signal = receiver.Receiver()
    alarm_bot = SlackAlarmBot()

    while 1:
        #activation_request = received_signal.check_input_from_keyboard()
        slack_request = alarm_bot.check_input_dummy()
        switch_request = received_signal.check_engage_switch()

        if slack_request:
            activation_request = slack_request
        else:
            activation_request = switch_request

        print("Activation request = ", activation_request)
        relay.activate(activation_request)
        print("sleep")
        await asyncio.sleep(0.4)


def run():
    print("Hi, I am the brain")

    alarm_bot = SlackAlarmBot()

    loop = asyncio.get_event_loop()
    loop.create_task(do_work())
    # loop.create_task(alarm_bot.rtm_client.start())

    loop.run_forever()
    loop.close()


if __name__ == '__main__':
    exit(run())
