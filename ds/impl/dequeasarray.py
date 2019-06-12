'''
Created on 11 Jun 2019

@author: anointedone
'''
from ds.impl.queueasarray import QueueAsArray
from adt.deque import Deque
from adt.exceptions.exceptions import ContainerFull, ContainerEmpty
from __builtin__ import None

class DequeAsArray(QueueAsArray,Deque):
    """
        
    """


    def __init__(self, size=0):
        '''
        Constructor
        '''
        super(DequeAsArray, self).__init__(size)
        
    def enqueueHead(self,obj):
        """Add `obj` at the head of the queue
        
            Raises:
                `ContainerFull`
        
            Notes:
            ------
            The process is based on the position if the head(`self._head`).
            Sets the head to the last index of the underlying array 
            (`self._array`),
            if the current position of the head is zero, otherwise
            decrements the head by 1.
            
            The underlying array is updated based on the modified head
            by inserting the `obj` at the array index determined by the
            head
            
            The container count(`self._count`) is then incremented by 1
        
        """
        if self._count == len(self._array):
            raise ContainerFull
        if self._head == 0:
            self._head = len(self._array)-1
        else:
            self._head = self._head -1
        self._array[self._head] = obj
        self._count += 1 
        
        #=======================================================================
        # `dequeTail` and `getTail` methods
        #=======================================================================
        
        def getTail(self):
            """Returns the object at the tail end of the queue
                Raises:
                -------
                    `ContainerEmpty`
                    
                Returns:
                --------
                    object
                Notes:
                ------    
                object in queue is returned based on the position
                of the tail, which is used as the index in the container
                array `self._array`
                
            """
            if self._count == 0:
                raise ContainerEmpty
            return self._array[self._tail]
        
        def enqeueTail(self,obj):
            if self._count == len(self._array):
                raise ContainerFull
            if self._tail == 0:
                self._tail = len(self._array) -1
            else:
                self._tail = self._tail -1
            self._array[self._tail] = obj
            self._count += 1
        def dequeueTail(self):
            """ removes object at the tail of the queue, returning the
                object removed
                Raises:
                -------
                    `ContainerEmpty`
                Returns:
                --------
                    object: 
                Notes:
                ------
                Before removal, the tail is temporarily saved in a local
                variable, then the underlying array is set to `None` at
                using the current position of the tail as index.
                
                The position of the tail is adjusted based on zero, wherein
                the tail is set to the last index of the underlying array
                by taking it's length -1, but if not zero, the tail is decremented
                by 1
                
                The count of the content in the queue is decremented by 1 before 
                the saved local var is then returned to the caller
            """
            if self._count == 0:
                raise ContainerEmpty()
            result = self._array[self._tail]
            self._array[self._tail] = None
            if self._tail == 0:
                self._tail = len(self._array)-1
            else:
                self._tail = self._tail -1
            self._count -= 1
            return result
            
        