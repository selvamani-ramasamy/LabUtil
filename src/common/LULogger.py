'''
Created on Jun 7, 2018

@author: selvamani ramasamy
'''

import logging

''' initialize logger '''
logging.basicConfig()
logger = logging.getLogger()

def getLogger():
    return logging.getLogger()

def setLogLevel(level):
    logger.setLevel(level)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def logCritical(message):
    logger.critical(message)

def logError(message):
    logger.error(message)

def logWarning(message):
    logger.warning(message)

def logInfo(message):
    logger.info(message)

def logDebug(message):
    logger.debug(message)

class MyClass(object):
    ''' Constructor '''
    def __init__(self, params):
        ''' nothing to do for now'''