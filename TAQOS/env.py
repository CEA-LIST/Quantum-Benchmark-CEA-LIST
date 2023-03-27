#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Define environment variables
=========
"""

# third party import
import os

# local import

# Project path to TAQOS directory
PROJECT_PATH = os.path.join('xxxx') # Put your path to TAQOS directory

###################################################
# Constants used for classical heuristics
###################################################
RTSEC = 1

###################################################
# Constants used specifically by the D-Wave system
###################################################

# Token used to solve problems with D-Wave
# You can get an account by signing up on:
# https://cloud.dwavesys.com/leap/login/?next=/leap/
DWAVE_TOKEN = 'xxxx' # Put your token here

# Default number of shots for each call to D-Wave
DW_NUM_READS = 256

# Default annealing time
DW_AN_TIME = 100
