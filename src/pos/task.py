import string
from typing import Text
from faker import Faker
from pos.models import Menu
from core.settings import CELERY_LOGGER
from celery import shared_task
from core.settings import SLACK_API_TOKEN
from slack import WebClient
from slack.errors import SlackApiError

fake = Faker()


@shared_task
def slack_notification(id):
    client = WebClient(token=SLACK_API_TOKEN)

    try:
        client.chat_postMessage(
            channel="#general",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Hey! :wave: Check you our menu's options :cook: for today... {id}",
                    },
                },
            ],
        )
    except SlackApiError as e:
        CELERY_LOGGER.error(f"Got an error: {e.response['error']}")
        return None

    message = "{} notification has been sent!".format(1)
    CELERY_LOGGER.info(message)
    return message
