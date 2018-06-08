'''
Created on Jun 6, 2018

@author: sramasam
'''

import os
from xml.dom.minidom import parse
import xml.dom.minidom

from LLogger import logCritical
from LLogger import logError
from LLogger import logDebug 

from Eredan import Eredan
from Caliondo import Caliondo

class Lab(object):
    '''
    classdocs
    '''
    deviceList = []
    name = None
    labFile = None

    def __init__(self, labFilePath):
        '''
        Constructor
        '''
        self.labFile = labFilePath
        self.parseLabConfig()

    def addDevice(self, device):
        self.deviceList.append(device)

    def removeDevice(self, deviceName):
        for device in self.deviceList:
            if (device.name == deviceName):
                self.deviceList.remove(device)
            else:
                print ("The device \'%s\'is not found in the Lab %s" %deviceName %self.name)

    def getDevice(self, sequence):
        if (sequence <= 0) or (sequence > len(self.deviceList)):
            print ("Error: device is not available")
            return

        device = self.deviceList[sequence -1]
        if device is not None:
            return device

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
    
    def parseLabConfig(self):
        #DOMTree = xml.dom.minidom.parse("config/lab.xml")
        #print (XMLFILES_FOLDER + "lab.xml")
        #DOMTree = xml.dom.minidom.parse(XMLFILES_FOLDER + "lab.xml")
        print ("parsing : %s" %self.labFile)
        DOMTree = xml.dom.minidom.parse(self.labFile)
        root = DOMTree.documentElement
    
        nodeLabs = root.getElementsByTagName("lab")
        for nodeLab in nodeLabs:
            #lab = Lab()
            if nodeLab.hasAttribute("id"):
                logDebug("lab id: %s" %nodeLab.getAttribute("id"))
                #lab = Lab(nodeLab.getAttribute("id"))
                self.name = nodeLab.getAttribute("id")
            #lab.name = labElement.getAttribute("id")

            duts = nodeLab.getElementsByTagName("dut")
    
            for dut in duts:
                #device = None
                dutName = dut.getElementsByTagName('name')[0]
                dutType = dut.getElementsByTagName('type')[0]
                mgmtAccess = dut.getElementsByTagName('management_access')[0]
                consoleAccess = dut.getElementsByTagName('console_access')[0]
                configFile = dut.getElementsByTagName('config_file')[0]
    
                if dutType.childNodes[0].data == 'eredan':
                    '''  name '''
                    if len(dutName.childNodes) == 1:
                        device = Eredan(dutName.childNodes[0].data)
                    else:
                        logCritical("device name can not be left empty")
                        exit (0)
                elif dutType.childNodes[0].data == 'caliondo':
                    #device = Caliondo()
                    '''  name '''
                    if len(dutName.childNodes) == 1:
                        device = Caliondo(dutName.childNodes[0].data)
                    else:
                        logCritical("device name can not be left empty")
                        exit (0)
    
                else:
                    logError("Invalid device type : %s " %dutType.childNodes[0].data)
                    exit (0)
    
                ''' type '''
                if len(dutType.childNodes) == 1:
                    device.type = dutType.childNodes[0].data
                else:
                    logCritical("device type for device %s can not be left empty" %device.name)
                    exit (0)
    
                ''' management access '''
                if len(mgmtAccess.childNodes) == 1:
                    device.managementAccess = mgmtAccess.childNodes[0].data
                else:
                    logCritical("management access for device %s is not available " %device.name)
                    exit (0)
    
                ''' console access '''
                if len(consoleAccess.childNodes) == 1:
                    device.consoleAcccess = consoleAccess.childNodes[0].data
    
                ''' console access '''
                if len(configFile.childNodes) == 1:
                    device.defaultConfig = configFile.childNodes[0].data
    
                self.addDevice(device)
                logDebug ("adding dut: %s" %(device.name + " : " + self.name))
