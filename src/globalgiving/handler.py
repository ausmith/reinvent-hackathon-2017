"""
Lambda handler for global giving

Author: Mindo, Aaron, Kavita, David
"""
# -*- coding: utf-8 -*-

import os
import logging
import json
from src.common.registration import Registration
from twilio.twiml.messaging_response import Body, Message, MessagingResponse

twilio_sid_register = os.environ['twilio_sid_register']
twilio_sid_update = os.environ['twilio_sid_update']
twilio_auth_token_register = os.environ['twilio_auth_token_register']
twilio_auth_token_update = os.environ['twilio_auth_token_update']

logging.basicConfig()
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)


def register_globalgiving(event, context):
    log.info(event)
    response = MessagingResponse()
    message = Message()

    reg = Registration(event)

    result = None
    if reg.execute():
        message.body("6782646400")
        response.append(message)
        result = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml"
            },
            "body": json.dumps(response)
        }
    else:
        message.body("6782646400")
        response.append(message)
        result = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml"
            },
            "body": json.dumps(response)
        }

    return result


def update_globalgiving(event, context):
    log.info(event)
