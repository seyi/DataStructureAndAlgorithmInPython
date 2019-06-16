'''
Created on 16 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.searchablecontainer import SearchableContainer
from datastructureandalgorithminpython.adt.abstractmethod import abstractmethod

class HashTable(SearchableContainer):
    ''' A searchable container which facilitates, putting, finding and removing of objects
    
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(HashTable, self).__init__()
        
    def __len__(self):
        pass
    __len__ = abstractmethod(__len__)
    
    def getLoadFactor(self):
        return self._count / len(self)
    loadFactor = property(
        fget = lambda self: self.getLoadFactor())
    
    def f(self,obj):
        """ Maps key into integers"""
        return hash(obj)
    def g(self,x):
        """ Maps non-negative integers into a set in the range of a positive constant M"""
        return abs(x) % len(self)
    
    def h(self,obj):
        """ A composition of meth:`f` and meth:`g`"""
        return self.g(self.f(obj))
        