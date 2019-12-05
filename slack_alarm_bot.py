import os
import slack


class SlackAlarmBot:

    alarm_on = False;

    def __init__(self):
        slack_token = "xoxb-225841683220-853263508177-bDaFlG3HW4EhW9ddELXaI2oy"
        self.rtm_client = slack.RTMClient(token=slack_token)
        self.rtm_client.on(event='message', callback = lambda **kwargs : self.say_hello(**kwargs))
        self.rtm_client.start()

    def say_hello(self, **payload):
        data = payload['data']
        web_client = payload['web_client']
        rtm_client = payload['rtm_client']
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
