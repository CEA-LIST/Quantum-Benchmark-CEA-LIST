#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Configuration of the logging device
=========

"""

# third party import
import logging
# local import
import sys


def log_debug(msg):
    """
    Write the message msg in the logger
    """
    logging.getLogger().debug(msg)


def create_logger():
    """
    Creation of the logging device, ignoring with logging level set to
    WARNING
    """
    logging.basicConfig(level=logging.WARNING)
    logging.getLogger('dwave.cloud.client.base').setLevel(logging.CRITICAL)
