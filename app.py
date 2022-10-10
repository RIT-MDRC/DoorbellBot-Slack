import asyncio
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command("/door")
def door_command(ack, body, client):
    try:
        response = requests.get(f'http://{os.environ["IP_ADDRESS"]}/door')
        out = response.text
    except:
        out = "Oops! Something went wrong"
    user_id = body["user_id"]
    ack(f"{out}, <@{user_id}>!")


@app.command("/elevator")
def elevator_command(ack, body):
    try:
        response = requests.get(f'http://{os.environ["IP_ADDRESS"]}/elevator')
        out = response.text
    except:
        out = "Oops! Something went wrong"
    user_id = body["user_id"]
    ack(f"{out}, <@{user_id}>!")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
