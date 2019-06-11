'''
Created on May 26, 2019

@author: anointedone
'''
import inspect
from django.template.defaultfilters import length
class Array(object):
    '''
    classdocs
    '''

    def getData(self):
        return self._data
    data = property(fget = lambda self: self.getData())

    def getBaseIndex(self):
        return self._baseIndex
    def setBaseIndex(self,value):
        self._baseIndex = value
    baseIndex = property(fget = lambda self : self.getBaseIndex(),
                         fset = lambda self, value : self.setBaseIndex(value))


    def __init__(self, length = 0,baseIndex = 0):
        '''
        Constructor
        '''
        assert length >= 0
        self._data = [None]*length
        self._baseIndex = baseIndex

    def __copy__(self):
        result = Array(len(self._data))
        for i, datum in enumerate(self._data):
            result._data[i] = datum
        result._baseIndex = self._baseIndex
        return result

    def getOffset(self,index):
        offset = index - self.baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return offset

    def __getitem__(self,idx):
            return self._data[self.getOffset(idx)]

    def __setitem__(self,index,value):
        self._data[self.getOffset(index)] = value
    def __len__(self):
        print('called Array __len__ with %s'%len(self._data))
        return len(self._data)