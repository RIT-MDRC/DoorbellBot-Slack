# Author: Cameron Robinson
# Email: cvr8924@rit.edu
# Date: 10/10/22
# Slack App for calling doorbell bot

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


def http_call(path):
    try:
        response = requests.get(f'http://{os.environ["IP_ADDRESS"]}/{path}')
        out = response.text
    except:  # I want this to handle a broad range of errors ~CR
        out = "Oops! Something went wrong"
    else:
        if response.status_code != 200:
            out = "Oops! Something went wrong"
    return out


@app.command("/roomba-status")
def door_command(ack, body):
    out = http_call("roomba_status")
    user_id = body["user_id"]
    ack(f"{out}, <@{user_id}>!")


@app.command("/door")
def door_command(ack, body):
    out = http_call("door")
    user_id = body["user_id"]
    ack(f"{out}, <@{user_id}>!")


@app.command("/elevator")
def elevator_command(ack, body):
    out = http_call("elevator")
    user_id = body["user_id"]
    ack(f"{out}, <@{user_id}>!")


# Start Websocket Relationship with slack
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
