'''
Created on Jun 6, 2018

@author: selvamani ramasamy
'''

import sys
import time
import pexpect

from src.common.LULogger import logCritical
from src.common.LULogger import logDebug 

class Device(object):
    name = None
    managementAccess = None
    consoleAcccess = None
    configFile = None
    pe = None

    ''' constructor '''
    def __init__(self, deviceName):
        self.name = deviceName;

    ''' connect to management ip '''
    def connectToManagementAccess(self):
        short_sleep = 5
        long_sleep = 60
        max_retry = 50
        max_short_sleep_retry = 10
        sleeptime = short_sleep
        retry_ctr = 0
    
        while (True):
            self.pe = pexpect.spawn ("telnet " + self.managementAccess)
            try:
                self.pe.expect("login:")
                break
            except:
                if (retry_ctr < max_retry):
                    retry_ctr = retry_ctr + 1;
    
                    if (retry_ctr > max_short_sleep_retry):
                        sleeptime = long_sleep
    
                    print("login_pe: %s no response, retry %d times, time now is %s, will sleep for %d sec..."%
                            (self.managementAccess, retry_ctr, time.strftime('%H:%M:%S'), sleeptime))
    
                    time.sleep(sleeptime)
            else:
                break
        ''' login using gss and password '''
        while (True):
            try:
                self.pe.sendline ('gss')
                self.pe.expect ('Password:')
                self.pe.sendline ('pureethernet')
                self.pe.expect (">")
                self.pe.sendline("")
                # extract the prompt, which is the last line of the pe.before buffer
                self.pe.expect(">")
                ''' just remove these lines for silent login '''
                self.pe.sendline("\r")
                self.pe.interact()
                #self.pe.sendline("\r\n")
                break
            except:
                if (retry_ctr < max_retry):
                    retry_ctr = retry_ctr + 1;
                    ''' If it has retried for the max_short_sleep_retry times, it is time to sleep
                        longer. We typically need it for the 8700 case. '''
                    if (retry_ctr > max_short_sleep_retry):
                        sleeptime = long_sleep
        
                    print("login_pe: %s no response, retry %d times, time now is %s, will sleep for %d sec..."%
                            (self.managementAccess, retry_ctr, time.strftime('%H:%M:%S'), sleeptime))
        
                    time.sleep(sleeptime)
                else:
                    break
        
        res = self.pe.before.split('\n')
        # Turn this on for debug
        #self.pe.logfile=sys.stdout
        return(self.pe, res[1]+"> ")

    ''' connect to console access:'''
    def connectToConsoleAccess(self):
        short_sleep = 5
        long_sleep = 60
        max_retry = 50
        max_short_sleep_retry = 10
        sleeptime = short_sleep
        retry_ctr = 0
        connected = False
        while (connected == False):
            self.pe = pexpect.spawn ("telnet %s" %self.consoleAcccess)
            try:
                self.pe.sendline("\r")
                index = self.pe.expect(['>', 'login:'])
                if index == 0:
                    connected = True
                    ''' already logged in '''
                    self.pe.sendline("\r")
                    self.pe.interact()
                    ''' done with interact -- return '''
                    return
                elif index == 1:
                    connected = True
                    ''' login prompt con'''
            except:
                ''' retry logic '''
                if (retry_ctr < max_retry):
                    retry_ctr = retry_ctr + 1;
    
                    if (retry_ctr > max_short_sleep_retry):
                        sleeptime = long_sleep
    
                    print("login: %s no response, retry %d times, time now is %s, will sleep for %d sec..."%
                            (self.managementAccess, retry_ctr, time.strftime('%H:%M:%S'), sleeptime))
    
                    time.sleep(sleeptime)

        ''' login using gss and password '''
        while (True):
            try:
                self.pe.sendline ('gss')
                self.pe.expect ('Password:')
                self.pe.sendline ('pureethernet')
                self.pe.expect (">")
                self.pe.sendline("")
                # extract the prompt, which is the last line of the pe.before buffer
                self.pe.expect(">")
                ''' just remove these lines for silent login '''
                self.pe.sendline("\r")
                self.pe.interact()
                #self.pe.sendline("\r\n")
                ''' done with interact '''
                break
            except:
                if (retry_ctr < max_retry):
                    retry_ctr = retry_ctr + 1;
                    ''' If it has retried for the max_short_sleep_retry times, it is time to sleep
                        longer. We typically need it for the 8700 case. '''
                    if (retry_ctr > max_short_sleep_retry):
                        sleeptime = long_sleep
        
                    print("login_pe: %s no response, retry %d times, time now is %s, will sleep for %d sec..."%
                            (self.managementAccess, retry_ctr, time.strftime('%H:%M:%S'), sleeptime))
        
                    time.sleep(sleeptime)
                else:
                    break


    ''' login to the device using management ip '''
    def login(self):
        short_sleep = 5
        long_sleep = 60
        max_retry = 50
        max_short_sleep_retry = 10
        sleeptime = short_sleep
        retry_ctr = 0
    
        while (True):
            logDebug("logging into device :" + self.managementAccess)
            self.pe = pexpect.spawn ("telnet " + self.managementAccess)
            self.pe.logfile_read = sys.stdout
            self.pe.maxread = 2000
            #self.pe.delaybeforesend = 0.1 
            self.pe.delayafterread = 0.2 
            try:
                self.pe.expect("login:")
                break
            except:
                if (retry_ctr < max_retry):
                    retry_ctr = retry_ctr + 1;
    
                    if (retry_ctr > max_short_sleep_retry):
                        sleeptime = long_sleep
    
                    print("login_pe: %s no response, retry %d times, time now is %s, will sleep for %d sec..."%
                            (self.managementAccess, retry_ctr, time.strftime('%H:%M:%S'), sleeptime))
    
                    time.sleep(sleeptime)
            else:
                break
        ''' login using gss and password '''
        while (True):
            try:
                self.pe.sendline ('gss')
                self.pe.expect ('Password:')
                self.pe.sendline ('pureethernet')
                self.pe.expect (">")
                self.pe.sendline("")
                # extract the prompt, which is the last line of the pe.before buffer
                self.pe.expect(">")
                break
            except:
                if (retry_ctr < max_retry):
                    retry_ctr = retry_ctr + 1;
                    ''' If it has retried for the max_short_sleep_retry times, it is time to sleep
                        longer. We typically need it for the 8700 case. '''
                    if (retry_ctr > max_short_sleep_retry):
                        sleeptime = long_sleep
        
                    print("login_pe: %s no response, retry %d times, time now is %s, will sleep for %d sec..."%
                            (self.managementAccess, retry_ctr, time.strftime('%H:%M:%S'), sleeptime))
        
                    time.sleep(sleeptime)
                else:
                    break

        res = self.pe.before.split('\n')
        # Turn this on for debug
        #self.pe.logfile=sys.stdout
        return(self.pe, res[1]+"> ")

    '''
    # Extract matched pattern from "sendline" output.
    def send_command_get_value(self, cmd, pattern):
       self.pe.sendline (cmd)
       try:
          self.pe.expect(pattern)
          return self.pe.match.group(1)
       except:
          return ""
    '''

    ''' install software '''
    def installSoftware(self):
        ''' TODO: '''

    ''' login into the device '''
    def loadConfiguration(self, filePath):
        ''' parse file ane send it to device '''
        fileFullPath = filePath + '/' + self.name + '.config' 
        logDebug("loading config file: " + fileFullPath)

        try:
            file = open(fileFullPath, 'r')
            if file is not None:
                ''' login into the device '''
                self.login()
    
                line = file.readline()
                while (line):
                    #print line
                    self.pe.sendline(line)
                    self.pe.expect('>')

                    line = file.readline()

            ''' important to sleep here -- otherwise configuration will not be done properly ''' 
            #time.sleep(3)
        except:
            logCritical ("the config file %s is not available" %fileFullPath)
