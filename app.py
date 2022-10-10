import asyncio
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command("/door")
def door_command(ack, body):
    response = requests.get('http://129.21.121.208:8080/door')
    user_id = body["user_id"]
    ack(f"{response.text}, <@{user_id}>!")


@app.command("/elevator")
def elevator_command(ack, body):
    response = requests.get('http://129.21.121.208:8080/elevator')
    user_id = body["user_id"]
    ack(f"{response.text}, <@{user_id}>!")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
