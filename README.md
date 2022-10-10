# DoorbellBot-Slack

This is the Slack Application for doorbell bot.

It adds the following commands to slack

* /door - calls roomba to door
* /elevator - calls roomba to elevator

## Environment Variables
This robot needs the following environment variables passed as parameters at runtime

| Name | Value |
| --- | --- |
| PYTHONUNBUFFERED | 1 |
| SLACK_BOT_TOKEN | *See doorbell-bot slack channel for tokens* |
| SLACK_APP_TOKEN | *See doorbell-bot slack channel for tokens* |
| IP_ADDRESS | 129.21.121.208:8080 |

## Additional Information
This app can only run when the roomba server is on. It should, however, handle errors from the server gracefully.

## To Do
Add safe disconnect handling
Update IP to raspberry pi IP

## Author
Cameron Robinson

cvr8924@rit.edu

