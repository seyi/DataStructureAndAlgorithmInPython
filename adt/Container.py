'''
Created on May 25, 2019

@author: anointedone
'''
from adt.abstractmethod import abstractmethod
from adt.visitor import Visitor

class Container(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Container,self).__init__()
        self._count = 0

    def purge(self):
        pass
    purge = abstractmethod(purge)

    def getCount(self):
        return self._count

    count = property(
                     fget = lambda self : self.getCount())

    def getIsEmpty(self):
        return self.count == 0

    isEmpty = property(
                       fget = lambda self: self.getIsEmpty())

    def getIsFull(self):
        return False

    isFull = property(
                     fget = lambda self : self.getIsFull())
    
    def accept(self,visitor):
        assert(isinstance(visitor, Visitor))