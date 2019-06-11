'''
Created on 10 Jun 2019

@author: anointedone
'''
from adt.array import Array
from adt.queue import Queue
from adt.exceptions.exceptions import ContainerFull, ContainerEmpty
class QueueAsArray(Queue):
    """
    A concrete Queue class
    
    Parameters
    ----------
    size : int
        Maximum number of items that can be stored in a queue
        Attributes
        ----------
        _array : array_like
            Used to hold content of the queue in a contiguous range of array element
            
        _head : int
            Denotes the left end of the queue
        _tail : int
            Denotes the right end of the queue
    Notes
    -----
        The region of contiguous elements will not necessarily occupy the leftmost positions.
        As elements are deleted at the head, the, the position of the left end will change
        Similarly, as elements are added at the tail, the position of the right end will change.
        In some circumstances, the contiguous region will wrap around the ends 
        of the array    
        When the queue contains only one element, then the head = tail
        
        If the queue is empty, the _head position will actually be to the right of the tail position
        However,this is also the same condition that arises when the queue is full!!
    """


    def __init__(self, size=0):
        '''
        Constructor
        '''
        super(QueueAsArray, self).__init__()
        self._array = Array(size)
        self._head = 0
        self._tail = size -1
        
    def purge(self):
        """ Removes all the contents of the Queue
            Notes:
            -----
                Walks through the occupied array positions assigning
                to each one the value `None` as it goes
                Running time is O(n) where n = `self._count`
        """
        while self._count > 0:
            self._array[self._head] = None
            self._head = self._head + 1
            if self._head == len(self._array):
                self._head = 0
            self._count -= 1
            
    def getHead(self):
        """ Overrides abstract `Queue.getHead` method 
            Raises:
                `ContainerEmpty`exception
            Returns:
            -------
                object
                 at the head position of the queue
        """
        if self._count == 0:
            raise ContainerEmpty
        return self._array[self._head]
    
    def enqueue(self,obj):
        """ Adds `obj` to the queue
            
            Raises:
            ------
            `ContainerFull` exception if the `self._count` attribute is 
            equal to the length of the underlying array (`self._array`)
            
            Notes:
            ------
            The tail(`self._tail`) position is used to determine where the
            new element will be added to the array.
            
            This is done by first incrementing the tail by 1 and checkking 
            the incremented tail value with the length of the array
            
            If the check is equal, the tail is set to 0, otherwise the obj is inserted
            at the current tail position
            
            Finally the count attribute `self._count` is incremented by 1
        
        """
        if self._count == len(self._array):
            raise ContainerFull()
        self._tail = self._tail + 1
        if self._tail == len(self._array):
            self._tail = 0
        self._array[self._tail] = obj
        self._count = self._count + 1
        
    def dequeue(self):
        """ Removes an obj from the head position of the queue
            Raises:
                `ContainerEmpty` exception
                
            Returns:
            -------
                object at the head position of the queue
                
            Notes:
            ------
            Saves the object at the head position in the `result` variable
            Sets the head(`self._head`) to 0 if the current value of head
            is equal to the length of the underlying array, 
            
            decrements the count and returns the result saved earlier
        """
        
        if self._count == 0:
            raise ContainerEmpty()
        result = self._array[self._head]
        self._array[self._head] = None
        self._head += 1
        if self._head == len(self._array):
            self._head = 0
        self._count -= 1
        return result
        
        
        