"""
Lambda handler for global giving

Author: Mindo, Aaron, Kavita, David
"""
# -*- coding: utf-8 -*-

import os
import logging
import json
from src.common.registration import Registration
from src.common.update import Update
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
            "body": str(response)
        }
    else:
        message.body("try again")
        response.append(message)
        result = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml"
            },
            "body": str(response)
        }

    return result


def update_globalgiving(event, context):
    log.info(event)
    response = MessagingResponse()
    message = Message()

    reg = Update(event)

    result = None
    if reg.execute():
        message.body("ack")
        response.append(message)
        result = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml"
            },
            "body": str(response)
        }
    else:
        message.body("try again")
        response.append(message)
        result = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/xml"
            },
            "body": str(response)
        }

    return result
