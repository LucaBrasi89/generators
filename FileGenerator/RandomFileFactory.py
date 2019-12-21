'''
Created on Dec 21, 2019

@author: andrew
'''
from FileGenerator.RandomFileService import RandomFileService
from FileGenerator.RandomFile import RandomFile

class RandomFileFactory(object):
    '''
    classdocs
    '''
    
    def makeModels(self, count):
        
        files = []
        
        for elem in range(count):
            
            name = RandomFileService.genRandFileName(16)
            ext = 'txt'
            date = RandomFileService.genRandDate()
            
            rf = RandomFile(name, ext, date)
            
            files.append(rf)
            
        return files


if __name__ == '__main__':
    
    factory = RandomFileFactory()
    models = factory.makeModels(3)
    import os
    os.chdir("/tmp")
    for model  in models:
        print(model)
        RandomFileService.createFile(model)
    

        
        
        
