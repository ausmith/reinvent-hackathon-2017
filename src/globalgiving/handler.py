"""
Lambda handler for global giving

Author: Mindo, Aaron, Kavita, David
"""
# -*- coding: utf-8 -*-

import os
import logging
# from twilio.rest import Client

twilio_sid_register = os.environ['twilio_sid_register']
twilio_sid_update = os.environ['twilio_sid_update']
twilio_auth_token_register = os.environ['twilio_auth_token_register']
twilio_auth_token_update = os.environ['twilio_auth_token_update']

logging.basicConfig()
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)


def post_globalgiving(event, context):
    log.info(event)
    handleEvent(event)


def handleEvent(event):
    """
        We want to handle all of our
    """
    if event['type'] == 'create':
        pass
    elif event['type'] == 'update':
        pass
    else:
        raise Exception('Request type is not allowed')
