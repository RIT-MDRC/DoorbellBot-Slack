import asyncio
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests


# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(say):
    print("Hi there!")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()




    #print("test")
    #asyncio.run(doShit())


