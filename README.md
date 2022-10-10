# DoorbellBot-Slack

This is the Slack Application for doorbell bot. The executable for this app is `app.py`.

It adds the following commands to slack

* `/door` - calls roomba to door
* `/elevator` - calls roomba to elevator

## Environment Variables
This robot needs the following environment variables passed as parameters at runtime.

| Name | Value |
| --- | --- |
| PYTHONUNBUFFERED | 1 |
| SLACK_BOT_TOKEN | *See doorbell-bot slack channel for tokens* |
| SLACK_APP_TOKEN | *See doorbell-bot slack channel for tokens* |
| IP_ADDRESS | 129.21.121.208:8080 |

## Additional Information
This app can only run when the roomba server is on. It should, however, handle errors from the server gracefully.

It is possible tokens may need to be updated. I don't know how to do that. If it has to happen I wish you good luck.

## To Do
Add safe disconnect handling
Update IP to raspberry pi IP
Figure out if tokens get updated
Make bash script to run app

## Author
Cameron Robinson

cvr8924@rit.edu

