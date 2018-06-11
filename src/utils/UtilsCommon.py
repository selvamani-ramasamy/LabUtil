'''
Created on Jun 7, 2018

@author: sramasam
'''

import os
import sys
import logging

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
LAB_XML_FILE = PROJECT_ROOT + "/config/lab.xml"

from src.common.LULogger import setLogLevel

''' possible values: CRITICAL   ERROR  WARNINIG  INFO  DEBUG '''
setLogLevel(logging.DEBUG)

