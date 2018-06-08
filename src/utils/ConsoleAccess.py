'''
Created on Jun 6, 2018

@author: sramasam
'''
import os

from src.utils import UtilsCommon
from src.utils.UtilsCommon import LAB_XML_FILE_PATH

#PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
#XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, '../config/')

import logging
from src.common.LLogger import setLogLevel

from src.common.Lab import Lab


#labFilePath = "/Users/sramasam/Documents/1.Selva/e-workspace/LabUtil/config/lab.xml"
labFilePath = LAB_XML_FILE_PATH

if __name__ == '__main__':
    ''' possible values: CRITICAL   ERROR  WARNINIG  INFO  DEBUG '''
    setLogLevel(logging.DEBUG)
    ''' initialize the lab '''
    labItem = Lab(labFilePath)

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

