'''
Created on 11 Jun 2019

@author: anointedone
'''
from adt.queue import Queue
from adt.abstractmethod import abstractmethod

class Deque(Queue):
    '''
    Notes:
    -----
        An extension of the Queue which provides a means to insert 
        and remove items at both end of the queue
        The word deque is an acronym for double-ended-queue
        
        A dequeue provids operations which access the head of the 
        queue, Head, enqueueHead and dequeHead. In the same fashion 3 
        operations for the tail, tail,enqueueTail and dequeuTail
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Deque, self).__init__()
        
        def getHead():
            pass
        getHead = abstractmethod(getHead)
        
        head = property(
                    fget = lambda self : self.getHead())
        
        def getTail(self):
            pass
        getTail = abstractmethod(getTail)
        
        tail = property(
            fget = lambda self: self.getTail())
        
        def enqueueHead(self, obj):
            pass
        enqueueHead = abstractmethod(enqueueHead)
        def dequeueHead(self):
            return self.dequeue()
        dequeueHead = abstractmethod(dequeueHead)
        
        def enqueueTail(self, object):
            self.enqueue(object)
        enqueueTail = abstractmethod(enqueueTail)
        def dequeueTail(self):
            return self.dequeue()
        dequeueTail = abstractmethod(dequeueTail)
         
            
        