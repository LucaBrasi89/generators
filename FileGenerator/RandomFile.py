'''
Created on Dec 21, 2019

@author: andrew
'''
class RandomFile(object):
    '''
    classdocs
    '''
 
    def __init__(self, name, ext, ctime):
        
        self.fileName = name + '.' + ext
        self.ctime = ctime
        
        
    def __str__(self):
        
        
        return 'fileName='+self.fileName+', ctime='+str(self.ctime)+ ')'

                
        
        
