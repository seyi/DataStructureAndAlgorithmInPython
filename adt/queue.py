'''
Created on 10 Jun 2019

@author: anointedone
'''
from adt.Container import Container
from adt.abstractmethod import abstractmethod

class Queue(Container):
    '''
    Single-ended queue, unlike a stack, elements are added at one end and removed at the other
    a first-in-first-out(FIFO) data structure
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Queue, self).__init__()
    
    def getHead(self):
        pass
    getHead = abstractmethod(getHead)
    def enqueue(self,obj):
        pass
    enqueue = abstractmethod(enqueue)
    def dequeue(self):
        pass
    enqueue = abstractmethod(dequeue)
    
    
        