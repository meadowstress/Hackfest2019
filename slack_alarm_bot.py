import os
import slack
import time

import asyncio
from multiprocessing import Pool

class SlackAlarmBot:

    alarm_on = False;

    def __init__(self):
        slack_token = os.environ['SLACK_API_TOKEN']
        self.rtm_client = slack.RTMClient(token=slack_token, run_async=True)
        self.rtm_client.on(event='message', callback =  self.say_hello)

    def say_hello(self, **payload):
        data = payload['data']
        web_client = payload['web_client']
        if 'Hello' in data.get('text', []):
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']

            web_client.chat_postMessage(
                channel=channel_id,
                text=f"Hi <@{user}>!",
                thread_ts=thread_ts
            )
        if 'Alarm' in data.get('text', []):
            self.alarm_on = True

    def check_input_dummy(self):
        return self.alarm_on;

async def foo():
    while True:
        print("say hi")
        await asyncio.sleep(5)

if __name__ == "__main__":

    alarm_bot = SlackAlarmBot()
    loop = asyncio.get_event_loop()
    loop.create_task(alarm_bot.rtm_client.start())
    loop.create_task(foo())
    loop.run_forever()
    loop.close()


