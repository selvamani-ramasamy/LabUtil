'''
Created on Jun 7, 2018

@author: sramasam
'''

import logging

''' initialize logger '''
logging.basicConfig()
logger = logging.getLogger()

def getLogger():
    return logging.getLogger()

def setLogLevel(level):
    logger.setLevel(level)
    #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def logCritical(message):
    logger.critical(message)

def logError(message):
    logger.error(message)

def logWarning(message):
    logger.warning(message)

def logInfo(message):
    logger.info(message)
'''
def logDebug(message):
    logger.warning(message)
'''
debug = False
def logDebug(message):
    if debug == True:
        print message
        

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        