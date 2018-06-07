'''
Created on Jun 6, 2018

@author: sramasam
'''

class Device(object):
    name = None
    managementAccess = None
    consoleAcccess = None
    configFile = None

    def __init__(self, deviceName):
        '''
        Constructor
        '''
        self.name = deviceName;

    def connectToManagementAccess(self):
        ''' connect to management ip '''

    def connectToConsoleAccess(self):
        ''' connect to console access:'''

    def installSoftware(self):
        ''' install software '''

    def loadConfiguration(self):
        ''' load the configuration file '''
