'''
Created on May 29, 2019

@author: anointedone
'''
from array import Array
from _ctypes import ArgumentError


class MultiDimensionalArray(Array):
    '''
    classdocs
    '''


    def __init__(self, *dimensions):
        '''
        Constructor
        '''
        self._dimensions = Array(len(dimensions))
        self._factors = Array(len(dimensions))
        product = 1
        i = len(dimensions) -1
        while  i >= 0:
            self._dimensions[i] = dimensions[i]
            self._factors[i] = product
            product *= self._dimensions[i]
            i -= 1
        self._data = Array(product)
        
    def getOffset(self, indices):
        assert(isinstance(self._dimensions, Array))
        if len(indices) != len(self._dimensions):
            raise IndexError
        offset = 0
        for i , dim in enumerate(self._dimensions):
            if indices[i] < 0 or indices[i] >= dim:
                raise IndexError
            offset += self._factors[i] * indices[i]
        return offset
    data = property(
        fget = lambda self : self.getData())
    
    def __getitem__(self, indices):
        assert(isinstance(indices,tuple))
        return self._data[self.getOffset(indices)]
    def __setitem__(self, index, value):
        self._data[self.getOffset(index)] = value


