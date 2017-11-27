"""
Lambda handler for global giving

Author: Mindo, Aaron, Kavita, David
"""
# -*- coding: utf-8 -*-

import os
import logging
from src.common.registration import Registration
from twilio.twiml.messaging_response import MessagingResponse

twilio_sid_register = os.environ['twilio_sid_register']
twilio_sid_update = os.environ['twilio_sid_update']
twilio_auth_token_register = os.environ['twilio_auth_token_register']
twilio_auth_token_update = os.environ['twilio_auth_token_update']

logging.basicConfig()
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)


def register_globalgiving(event, context):
    log.info(event)
    resp = MessagingResponse()
    reg = Registration(event)

    if reg.validateData():
        resp.message("6782646400")
    else:
        resp.message("Try again")

    return str(resp)


def update_globalgiving(event, context):
    log.info(event)
