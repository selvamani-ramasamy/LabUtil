'''
Created on Jun 6, 2018

@author: selvamani ramasamy
'''

from UtilsCommon import *
from src.common.Lab import Lab
from src.common.LULogger import logDebug

if __name__ == '__main__':
    ''' initialize the lab - change the file path in UtilsCommon.py'''
    labItem = Lab(LAB_XML_FILE)

    if labItem.validateConfigPath() == False:
        exit (0)

    baseConfigPath = PROJECT_ROOT + "/" + labItem.baseConfigPath
    deviceConfigPath = PROJECT_ROOT + "/" + labItem.configPath

    val  = ""
    while((val != 'quit') or (val !='q')):
        labItem.showLab()
        print ""
        val = raw_input('Select a device using S.No (q/quit) or all:')

        if ((val == 'quit') or (val =='q')):
            break
        else:
            if (val == 'all'):
                for device in labItem.deviceList:
                    print "loading base config in device %s"%device.name
                    device.loadConfiguration(baseConfigPath)
                    #device.loadConfiguration(deviceConfigPath)

                break;
            else:
                selectedDevice = int(val)
                # get the device and do the operation
                labItem.showDevice(selectedDevice)
                ''' load base config '''
                logDebug("loading base config in device %s" %labItem.getDevice(selectedDevice))
                labItem.getDevice(selectedDevice).loadConfiguration(baseConfigPath)
                ''' load device config '''
                #labItem.getDevice(selectedDevice).loadConfiguration(deviceConfigPath)
                break;
