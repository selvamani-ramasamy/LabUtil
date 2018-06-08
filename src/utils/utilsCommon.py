'''
Created on Jun 7, 2018

@author: sramasam
'''

import os
import sys

''' set the project dirctory to PYTHONPATH ''' 
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)

LAB_XML_FILE_PATH = PROJECT_ROOT + "/config/lab.xml"