'''
Created on Jun 6, 2018

@author: selvamani ramasamy
'''

from UtilsCommon import *
from src.common.Lab import Lab

if __name__ == '__main__':
    ''' initialize the lab - change the file path in UtilsCommon.py'''
    labItem = Lab(LAB_XML_FILE)

    val  = ""
    while((val != 'quit') or (val !='q')):
        labItem.showLab()
        print ""
        val = raw_input('Select a device using S.No (q/quit):')

        if ((val == 'quit') or (val =='q')):
            break
        else:
            selectedDevice = int(val)
            # get the device and do the operation
            labItem.showDevice(selectedDevice)
            labItem.getDevice(selectedDevice).connectToConsoleAccess()

