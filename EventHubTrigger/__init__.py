import logging
import json
from twython import Twython
import os
import azure.functions as func

consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def sendTwitterMsg():
    message = "Hey Skippy, Kenny, and Willy, time for an Australian Christmas Day on the beach #25DaysOfServerless"
    try:
        twitter.update_status(status=message)
    except:
        logging.info("problem tweeting from the Python Function")
        logging.info("Tweeted: %s" % message)


def main(event: func.EventHubEvent):

    data = event.get_body().decode('utf-8')
    telemetry = json.loads(data)

    for item in telemetry:
        temperature = item.get("temperature")
        if temperature is not None and type(temperature) is float and 31 < temperature < 40:
            print(temperature)
            sendTwitterMsg()
