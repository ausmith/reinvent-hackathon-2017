"""
Lambda handler for global giving

Author: Mindo, Aaron, Kavita, David
"""
# -*- coding: utf-8 -*-

import os
# from twilio.rest import Client

twilio_sid_register = os.environ['twilio_sid_register']
twilio_sid_update = os.environ['twilio_sid_update']
twilio_auth_token = os.environ['twilio_auth_token']


def post_globalgiving(event, context):
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
