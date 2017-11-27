"""
Lambda handler for global giving

Author: Mindo, Aaron, Kavita, David
"""
# -*- coding: utf-8 -*-

import os
import logging
from src.common.registration import Registration
# from twilio.rest import Client

twilio_sid_register = os.environ['twilio_sid_register']
twilio_sid_update = os.environ['twilio_sid_update']
twilio_auth_token_register = os.environ['twilio_auth_token_register']
twilio_auth_token_update = os.environ['twilio_auth_token_update']

logging.basicConfig()
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)


def register_globalgiving(event, context):
    log.info(event)


def update_globalgiving(event, context):
    log.info(event)
