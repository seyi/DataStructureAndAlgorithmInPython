'''
Created on 12 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.olist import OrderedList
from adt.array import Array
from adt.exceptions.exceptions import ContainerFull, ContainerEmpty
from datastructureandalgorithminpython.position.cursor import Cursor
from termios import CERASE
from CoreGraphics._CoreGraphics import CGRect_getMidX

class OrderedListAsArray(OrderedList):
    ''' An array based implementation of an ordered list
        Extends:
        -------
        `OrderedList`
        
        Attributes:
        -----------
            `self._array` : Underlying array initialized by the `size` param
            
        
        Notes:
        Positioning in an an ordered list is determined by the index of the
        items in the array attribute. The first item is situated at index 0,
        while the last item is at index count - 1
        
        The items in the array have a successor,predecessor relationship structure where an item 
        at index i+1 is the successor of the item at i 
    '''


    def __init__(self, size=0):
        '''
        Constructor
        '''
        super(OrderedListAsArray, self).__init__()
        self._array = Array(size)
        
    def insert(self,obj):
        """ inserts an item into the ordered list
            items are inserted at the end of the list, which is determined by the count
            attribute
            
            Args:
                `obj` : item to be inserted
            Raises:
            -------
                `ContainerFull` exception
                
        """
        if self._count == len(self._array):
            raise ContainerFull
        self._array[self._count] = obj
        self._count += 1
        
    def __contains__(self,obj):
        """Tests whether `obj` is in the OrderedList
        
            Returns:
            --------
                boolean
            Notes:
            ------
                Runs a loop based on the number of elements in the 
                array object of the OrderedList.
                Compares each element with `obj` and returns True to
                stop the iteration
                
                Returns False if item is not found
        
        """
        for i in range(self._count):
            if self._array[i] is obj :
                return True
        return False
    def find(self,obj):
        """finds `obj` in the ordered list, returning obj
        
            Returns:
            --------
            object | None
        
            Notes:
            -----
                Iterates through the underlying array, based on the
                items in the array.
                Compares obj with item in the array and returns obj if
                comparison passes which halts the iteration process. Otherwise
                returns None if `obj` is not Found
        """
        for i in  range(self._count):
            if obj == self._array[i]:
                return self._array[i]
        return None
    
    def withdraw(self, obj):
        """withdraws `obj` from the `OrderedList`
            
            Raises:
            -------
                `KeyError`
            Notes:
            ------
                Uses count(`self._count`) attribute as Iteration limit.
                Implementation keeps track of the array(`self._array`) index,
                which had been incremented in the while loop. The index is the 
                position of the matched object(`obj`)
                
                Once a matched is found, a replacement of the items in the array
                is carried out in a while loop starting from the matched index, incrementing the
                index on the go
                
                Finally, the last element in the array is replaced with `None` and
                the count attribute (self._count) is decremented by 1
        """
        i = 0 
        while i < self._count and obj is not self._array[i]:
            i += 1
        if i == self._count:
            raise KeyError
        while i < self._count-1:
            self._array[i] = self._array[i + 1]
            i += 1
        self._array[i] = None
        self._count -= 1  
        
    def findPosition(self, obj):
        """ Finds the position of `obj` in the `OrderedList`
        
            Returns:
            --------
                `Cursor`
            
            Notes:
            ------
                Searches by using a while loop, based on the count
                attribute which is used as iteration limit.
                
                It uses the == operator as comparison, saves the index
                at the point where the comparison passes.
                
                A Cursor object with the  saved index as parameter is created and retuned.
                Based on comparison, a success saves the current index where the match
                occurs, while a failed search, creates a cursor object with 
                position that is same as the count ie out of index by 1
        
        """
        i = 0
        while i < self._count and self._array[i] != obj:
            i += 1
        return self.Cursor(self,i)
    
        
    
    def __getitem__(self, offset):
        if offset < 0 or offset >= self._count:
            raise IndexError
        return self._array[offset]
            
        
    class Cursor(Cursor):
        """An abstraction of position in an OrderedList instance
        
            Extends:
            --------
            `Cursor`
            Attributes:
            -----------
                _list : `OrderedListAsArray` instance
                _offset : `int`  records an offset in the _list array of objects
        """
        def __init__(self,mlist,offset):
            super(OrderedListAsArray.Cursor, self).__init__(mlist)
            self._offset = offset
            
        def getDatum(self):
            """returns the item of the cursor list, based on the offset
                
            """
            if self._offset < 0 \
                or self._offset >= self._list._count:
                raise IndexError
            return self._list._array[self._offset]
        
        def insertAfter(self, obj):
            """insert `obj` after the current Cursor position
                Notes:
                ------
                Uses a cursor instance with the ordered list as attributes
                passed in the constructor.
                
                Tests for a filled list and raises `ContainerFull` if test fails,
                Also tests for out of range errors by checking the offset arg passed
                to the cursor.
                
                The idea is to shift the elements of the list array at indices after the
                insertion point to the right in a while loop which uses the list count
                as base, decremented by 1 for every iteration 
                
                After the iteration, insertion is carried out at the
                insertion point, which was incemented by 1 earlier in the process insertionPoint = self._offset + 1 `self._list._array[insertionPoint] = obj`
                
                Usage:
                ------
                   `ol = OrderedListAsArray(4)
                    ol.insert(1)
                    ol.insert(2)
                    c = OrderedListAsArray.Cursor(ol,0)
                    c.insertAfter(3)
                    c2 = OrderedListAsArray.Cursor(ol,1)
                    #get the data just inserted
                    d = c2.getDatum()
                    assert(d == 3)`
            """
            if self._offset < 0 \
                or self._offset >= len(self._list._array):
                raise IndexError
            if self._list._count == len(self._list._array):
                raise ContainerFull()
            insertionPoint = self._offset + 1
            i = self._list._count
            while i > insertionPoint :
                self._list._array[i] = self._list._array[i-1]
                i -= 1
            self._list._array[insertionPoint] = obj
            self._list._count += 1
            
        def insertBefore(self, obj):
            """insert `obj` before the current Cursor position
                Notes:
                ------
                Uses a cursor instance with the ordered list as attributes
                passed in the constructor.
                
                Tests for a filled list and raises `ContainerFull` if test fails,
                Also tests for out of range errors by checking the offset arg passed
                to the cursor.
                
                The idea is to shift the elements of the list array at indices after the
                insertion point to the right in a while loop which uses the list count
                as base, decremented by 1 for every iteration.
                Kindly note that insertion point is the value of the cursor target, unlke the
                case of insertAfter where  1 is insertion point 
                After the iteration, insertion is carried out at the
                insertion point, which was incemented by 1 earlier in the process insertionPoint = self._offset + 1 `self._list._array[insertionPoint] = obj`
                
                Usage:
                ------
                    ol = OrderedListAsArray(4)
                    ol.insert(1)
                    ol.insert(3)
                    ol.insert(4)
                    c = OrderedListAsArray.Cursor(ol,1)
                    c.insertBefore(2)
                    c2 = OrderedListAsArray.Cursor(ol,3)
                    #get the data just inserted
                    d = c2.getDatum()
                    
                    assert(d == 4)
            """

            if self._list._count == len(self._list._array):
                raise ContainerFull()
            if self._offset < 0 \
                or self._offset >= len(self._list._array):
                raise IndexError
            insertionPoint = self._offset
            i = self._list._count
            while i > insertionPoint:
                self._list._array[i] = self._list._array[i-1]
                i -= 1
            self._list._array[insertionPoint] = obj
            self._list._count += 1
            
        def withdraw(self):
            if self._offset < 0 \
                or self._offset >= len(self._list._array):
                raise IndexError
            if self._list._count == 0:
                raise ContainerEmpty
            i = self._offset
            while i < self._list._count - 1:
                self._list._array[i] = self._list._array[i + 1]
                i += 1
                #++i
                
            self._list._array[i] = None
            self._list._count -= 1
            
             
        
        