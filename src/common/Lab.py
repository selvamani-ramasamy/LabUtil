'''
Created on Jun 6, 2018

@author: sramasam
'''
from Device import Device

class Lab(object):
    '''
    classdocs
    '''
    deviceList = []
    name = None

    def __init__(self, labName):
        '''
        Constructor
        '''
        self.name = labName

    def addDevice(self, device):
        self.deviceList.append(device)

    def removeDevice(self, deviceName):
        for device in self.deviceList:
            if (device.name == deviceName):
                self.deviceList.remove(device)
            else:
                print ("The device \'%s\'is not found in the Lab %s" %deviceName %self.name)

    def showLab(self):
        print ("lab name: %s" %self.name)
        print "~~~~~~~~~~~~~~~~~~~~~~~~~"
        print ("{0:<5} {1:15} {2:10} {3:15} {4:15}".format("S.No", "Name", "Type", "Mgmt Access", "Console Access"))
        #print ("Name\tType\tMgmt Access\tConsole Access \t")
        index = 0;
        for device in self.deviceList:
            index = index + 1
            print ("{0:<5} {1:15} {2:10} {3:15} {4:15}".format(index, device.name, device.type, device.managementAccess, device.consoleAcccess))
            
            '''
            print "dut name          : %s" %device.name
            print "dut dutType       : %s" %device.type
            print "dut mgmtAccess    : %s" %device.managementAccess
            print "dut consoleAccess : %s" %device.consoleAcccess
            print "dut configFile    : %s" %device.configFile
            print "--------------"
            '''

    def installSoftware(self):
        ''' install software for all devices '''
    
    def loadConfiguration(self):
        ''' load configuration in all devices '''
    
    def showDevice(self, sequence):
        if (sequence <= 0) or (sequence > len(self.deviceList)):
            print ("Error: device is not available")
            return

        device = self.deviceList[sequence -1]
        if device is not None:
            print ("{0:<5} {1:15} {2:10} {3:15} {4:15}".format(sequence, device.name, device.type, device.managementAccess, device.consoleAcccess))
