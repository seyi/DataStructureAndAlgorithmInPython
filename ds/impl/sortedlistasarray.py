'''
Created on 15 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.olist import OrderedList
from datastructureandalgorithminpython.adt.sortedtlist import SortedList
from adt.exceptions.exceptions import ContainerFull, ContainerEmpty
from datastructureandalgorithminpython.ds.impl.orderedlistasarray import OrderedListAsArray

class SortedListAsArray(OrderedListAsArray,SortedList):
    '''
    classdocs
    '''
    def __init__(self, size=0):
        '''
        Constructor
        '''
        super(SortedListAsArray, self).__init__(size)
        
    def insert(self,obj):
        """Inserts `obj` into the List
            Raises:
            -------
                `ContainerFull`
            Notes:
            ------
                Shifts the elements to the right if greater.
                While loop uses the count attributes, starting from 
                the count `self._count` index of the array decrementing the
                iteration base by 1 for each iteration.
                
                finally the count attribute(`self._count`) is incremented
                by 1
        """
        if self._count == len(self._array):
            raise ContainerFull
        i = self._count
        
        while i > 0 and self._array[i-1] > obj:
            self._array[i] = self._array[i - 1]
            i -= 1
        self._array[i] = obj
        self._count += 1
        
    def findOffset(self,obj):
        """finds the offset of `obj` in the `SortedList`
        
            Returns:
            --------
            `int`
            
            Notes:
            ------
                Uses a binary search algorithm
                First, the left and right points are determined
                with the left as the 0 and right as the number
                of items in the list ie `self._count`
                
                The iteration is based on the left point <= right
                condition. A middle point is dynamically determined
                and modified.
                If the object greater than the element at the middle,
                the left is reassigned to an index+1, so search is 
                to the `range(middle+1,right)`.
                
                But if the object is lower than middle element, right
                is reassigned to middle -1 and the process is repeated 
                till the offset of `obj` is found.
                
                IF nothing if found, -1 is returned
        
        """
        
        left = 0
        right = self._count - 1
        
        while left <= right:
            middle = (right + left)/ 2
            if obj > self._array[middle]:
                left = middle + 1
            elif obj < self._array[middle]:
                right = middle -1
            else:
                return middle
        return -1
    
    def find(self,obj):
        """Finds `obj` in the sorted List
        
            returns:
            --------
            object | None
        
            Notes:
            ------
            first method simply gets the position of the object
            and returns the object.
            
            The second method meth:`findPosition(self,obj)` returns a cursor
            The `SortedListAsarray.Cursor` is a derived class of the
            class:`OrderedListAsArray.Cursor`, which raises a error:
            `TypeError` on the meth:`Cursor.insertBefore` and 
            `Cursor.insertAfter` methods to prevent calls to those methods.
            
            The `SortedListAsarray.Cursor` is passed the offset returned by
            the meth:`findOffset(self,obj)` method
            
            
        
        """
        offset = self.findOffset(obj)
        #=======================================================================
        # if offset >= 0:
        #     return self._array[offset]
        # else:
        #     return None
        #=======================================================================
        return self._array[offset] if offset >= 0 else None
    
    class Cursor(OrderedListAsArray.Cursor):
        
        def __init__(self, mlist, offset):
            super(SortedListAsArray.Cursor, self) \
                .__init__(mlist,offset)
                
        def insertAfter(self, obj):
            raise TypeError
        
        def insertBefore(self, obj):
            raise TypeError
        
    def findPosition(self, obj):
        return self.Cursor(self,self.findOffset(obj))
    
    def withdraw(self, obj):
        """ Removes `obj` from the list
            
            Raises:
            -------
                exception:`ContainerEmpty`
                `KeyError`
            Notes:
            ------
            Makes use of the meth:`findOffset(self,obj)` method to 
            determine the position of `obj`.
            once position is determined, elements in the list is moved
            to the left, starting at the offset retrieved earlier in 
            a while loop which uses offset as base and nuber of items
            (`self._count`) as the stop condition
            
            the count attribute of the list is then decremented by 1 on
            a successful removal
            """
        if self._count == 0:
            raise ContainerEmpty
        offset = self.findOffset(obj)
        if offset < 0:
            raise KeyError
        
        while offset < self._count:
            self._array[offset] = self._array[offset+1]
            offset +=1
        self._array[offset] = None
        self._count -= 1
            
                
        
        