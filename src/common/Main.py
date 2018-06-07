'''
Created on Jun 6, 2018

@author: sramasam
'''
from xml.dom.minidom import parse
import xml.dom.minidom

import os
import logging

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, '../config/')

from Lab import Lab
from Device import Device
from Eredan import Eredan
from Caliondo import Caliondo


''' labs container '''
labList = []

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

def parseLabConfig():
    #DOMTree = xml.dom.minidom.parse("config/lab.xml")
    print (XMLFILES_FOLDER + "lab.xml")
    #DOMTree = xml.dom.minidom.parse(XMLFILES_FOLDER + "lab.xml")
    DOMTree = xml.dom.minidom.parse("/Users/sramasam/Documents/1.Selva/e-workspace/LabUtil/config/lab.xml")
    root = DOMTree.documentElement

    labs = root.getElementsByTagName("lab")

    '''
    for labElement in labs:
        if labElement.hasAttribute("id"):
            print ("lab id: %s" %labElement.getAttribute("id"))
            print ("-------------")
        duts = labElement.getElementsByTagName("dut")
        for dut in duts:
            device = Device()
            dutName = dut.getElementsByTagName('name')[0]

            if len(dutName.childNodes) == 1:
                device.name = dutName.childNodes[0].data
                print "device name : %s" %device.name
            else:
                print "device name can not be left empty"
                exit (0)

    exit (0)
    '''

    for labElement in labs:
        #lab = Lab()

        if labElement.hasAttribute("id"):
            logDebug("lab id: %s" %labElement.getAttribute("id"))
            lab = Lab(labElement.getAttribute("id"))
            #lab.name = labElement.getAttribute("id")

        duts = labElement.getElementsByTagName("dut")

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

            lab.addDevice(device)
            logDebug ("adding dut: %s" %(device.name + " : " + lab.name))

        ''' add the lab to lablist '''
        labList.append(lab)

if __name__ == '__main__':
    ''' possible values: CRITICAL   ERROR  WARNINIG  INFO  DEBUG '''
    setLogLevel(logging.DEBUG)

    parseLabConfig()

    labItem = labList[0]
#    for labItem in labList:
#        labItem.showLab()

    val  = ""
    while((val != 'quit') or (val !='q')):
        labItem.showLab()
        print ""
        val = raw_input('Select a device using S.No or (q to quit):')
        
        if ((val == 'quit') or (val =='q')):
            break
        else:
            selectedDevice = int(val)
            ''' get the device and do the operation '''
            labItem.showDevice(selectedDevice)
            