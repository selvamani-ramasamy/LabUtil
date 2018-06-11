'''
Created on Jun 6, 2018

@author: selvamani ramasamy
'''

#import os
#from xml.dom.minidom import parse
import xml.dom.minidom

from src.common.LULogger import logCritical
from src.common.LULogger import logError
from src.common.LULogger import logDebug 

from Eredan import Eredan
from Caliondo import Caliondo

class Lab(object):
    deviceList = []
    name = None
    labFile = None #xml file comprising lab information
    ftpServer = None
    tftpServer = None
    softPackageName = None
    softPackagePath = None
    baseConfigPath = None
    configPath = None

    ''' Constructor '''
    def __init__(self, labFilePath):
        self.labFile = labFilePath
        self.parseLabConfig()

    ''' add device to the list '''
    def addDevice(self, device):
        self.deviceList.append(device)

    ''' remove the device from the list '''
    def removeDevice(self, deviceName):
        for device in self.deviceList:
            if (device.name == deviceName):
                self.deviceList.remove(device)
            else:
                print ("The device \'%s\'is not found in the Lab %s" %deviceName %self.name)

    ''' get the device '''
    def getDevice(self, sequence):
        if (sequence <= 0) or (sequence > len(self.deviceList)):
            print ("Error: device is not available")
            return

        device = self.deviceList[sequence -1]
        if device is not None:
            return device

    ''' show lab information '''
    def showLab(self):
        print ("lab name: %s" %self.name)
        print "~~~~~~~~~~~~~~~~~~~~~~~~~"
        print ("ftp server       :%s" %self.ftpServer)
        print ("tftp server      :%s" %self.tftpServer)
        print ("package name     :%s" %self.softPackageName)
        print ("package path     :%s" %self.softPackagePath)
        print ("base config path :%s" %self.baseConfigPath)
        print ("config path      :%s" %self.configPath)
        print ""
        print "DUT info:"
        print "~~~~~~~~~~"
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

    ''' install Software for all devices '''
    def installSoftware(self):
        ''' TODO:  '''

    ''' load the configuration for all devices '''
    #def loadConfiguration(self):
    #    ''' TODO: '''

    ''' show all devices information '''
    def showDevice(self, sequence):
        if (sequence <= 0) or (sequence > len(self.deviceList)):
            print ("Error: device is not available")
            return

        device = self.deviceList[sequence -1]
        if device is not None:
            print ("{0:<5} {1:15} {2:10} {3:15} {4:15}".format(sequence, device.name, device.type, device.managementAccess, device.consoleAcccess))

    ''' parse lab config xml and populat the devices '''
    def parseLabConfig(self):
        logDebug ("parsing : %s" %self.labFile)
        DOMTree = xml.dom.minidom.parse(self.labFile)
        root = DOMTree.documentElement
    
        nodeLabs = root.getElementsByTagName("lab")
        for nodeLab in nodeLabs:
            if nodeLab.hasAttribute("id"):
                logDebug("lab id: %s" %nodeLab.getAttribute("id"))
                self.name = nodeLab.getAttribute("id")

            ''' parse lab_info '''
            labInfoNode = nodeLab.getElementsByTagName("lab_info")[0]
            if len(labInfoNode.childNodes) > 0:
                if len(labInfoNode.getElementsByTagName('ftp_server')[0].childNodes) == 1:
                    self.ftpServer = labInfoNode.getElementsByTagName('ftp_server')[0].firstChild.data
                if len(labInfoNode.getElementsByTagName('tftp_server')[0].childNodes) == 1:
                    self.tftpServer = labInfoNode.getElementsByTagName('tftp_server')[0].firstChild.data
                if len(labInfoNode.getElementsByTagName('package')[0].childNodes) == 1:
                    self.softPackageName = labInfoNode.getElementsByTagName('package')[0].firstChild.data
                if len(labInfoNode.getElementsByTagName('package_path')[0].childNodes) == 1:
                    self.softPackagePath = labInfoNode.getElementsByTagName('package_path')[0].firstChild.data
                if len(labInfoNode.getElementsByTagName('base_config_path')[0].childNodes) == 1:
                    self.baseConfigPath = labInfoNode.getElementsByTagName('base_config_path')[0].firstChild.data
                if len(labInfoNode.getElementsByTagName('config_path')[0].childNodes) == 1:
                    self.configPath = labInfoNode.getElementsByTagName('config_path')[0].firstChild.data

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
                logDebug ("adding dut: %s" %(device.name + " to lab: " + self.name))

    ''' check base config and config path entries '''
    def validateConfigPath(self):
        if self.baseConfigPath is None:
            logCritical("base config path is empty")
            return False

        if self.configPath is None:
            logCritical("config path is empty")
            return False

        return True

    ''' validate software package name and package path entries '''
    def validateSoftwarePackage(self):
        if self.softPackageName is None:
            logCritical("software package name is empty")
            return False

        if self.softPackagePath is None:
            logCritical("software package path is empty")
            return False

        return True