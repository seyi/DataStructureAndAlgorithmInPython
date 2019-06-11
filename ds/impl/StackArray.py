'''
Created on 6 Jun 2019

@author: anointedone
'''
from adt.stack import Stack
from adt.array import Array
from adt.visitor import Visitor
from adt.it import Iterator
from adt.exceptions.exceptions import ContainerFull, ContainerEmpty


class StackArray(Stack):
    '''
    Array based implementation of stacks
    '''


    def __init__(self, size = 0):
        '''
        Constructor
        '''
        super(StackArray, self).__init__()
        self._array = Array(size)
        
    def purge(self):
        """ Removes all the content of a container """
        while self._count > 0:
            self._array[self._count-1] = None
            self._count -= 1
            
    def push(self,obj):
        """ Add an element to the stack"""
        if self._count == len(self._array):
            raise ContainerFull
        self._array[self._count] = obj
        self._count += 1
        
    def pop(self):
        """ Removes an element from the top of the stack, returning the element to caller"""
        if self._count == 0:
            raise ContainerEmpty
        self._count -= 1
        result = self._array[self._count]
        self._array[self._count] = None
        return result
    
    def getTop(self):
        """ Get the element at the top of the stack without removing the element"""
        if self._count == 0:
            raise ContainerEmpty
        return self._array[self._count - 1]
    
    def accept(self, visitor):
        """ Accept a visitor instance for walking the stack and performing
            operation on each element
        """
        assert(isinstance(visitor,Visitor))
        for i in range(len(self._array) - 1):
            visitor.visit(self._array[i])
            if visitor.isDone:
                return
            
    def __iter__(self):
        """ The _iter__ method of a ontainer returns an Iterator"""
        return self.Iterator(self)
            
    #===========================================================================
    # Hooks
    #===========================================================================
    def __len__(self):
            return self._count     
    class Iterator(Iterator):
        """ Derived iterator class for the Derived StackArray container """
        def __init__(self,stack):
            super(StackArray.Iterator, self).__init__(stack)
            self._position = 0
            
        def next(self):
            """ Returns the next object in the stackarray based on the
                current position of the iterator, increments the iterator position
                Raises StopIteration Exception if requested position is equal or greater
                than the stackarray's count
            """
            if self._position >= self._container._count:
                raise StopIteration
            obj = self._container._array[self._position]
            self._position = self._position + 1
            return obj
        
        #=======================================================================
        # Hooks
        #=======================================================================
        
        

        