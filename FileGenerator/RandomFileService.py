'''
Created on Dec 21, 2019

@author: andrew
'''

import os, time, random, string
from win32_setctime import setctime
from pathlib import Path




class RandomFileService(object):
    '''
    classdocs
    '''
    @staticmethod
    def genRandFileName(stringLength):
        """Generate a random string with the combination of lowercase and uppercase letters """
    
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    
    
    
    @staticmethod
    def genRandDate():
        
        start = 976597720
        end = int(time.time())

        return random.randint(start, end)
    
    
    @staticmethod
    def createFile(model):
        
        Path(model.fileName).touch()   
        
    @staticmethod
    def setFileTime(model):
        
        setctime(model.fileName, model.ctime)
        os.utime(model.fileName, (model.ctime, model.ctime))
    
