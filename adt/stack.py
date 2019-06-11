'''
Created on May 25, 2019

@author: anointedone
'''
from Container import Container
from adt.abstractmethod import abstractmethod

class Stack(Container):
    '''
        LIFO data structure
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Stack, self).__init__()
    def getTop(self):
        pass
    getTop = abstractmethod(getTop)
    top = property(
        fget = lambda self : self.getTop())
    def push(self,obj):
        pass
    push = abstractmethod(push)
    def pop(self):
        pass
    pop = abstractmethod(pop)
    
    
