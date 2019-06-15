
Data structure and algorithm based on the Bruno.R.Preiss book (Data Structure and algorithm with object oriented design patterns in python) and the Goodrich, Tamassia,Goldwasser Book(Data Structure and Algorihm in Python)  Contains well documented source codes, partly modified and extensive unit testing


Ordered List
   An array based implementation of an ordered list
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
  Usage :
        ol  = OrderedListAsArray(5) 
        obj1 = [57]
        obj2 = [57]
        obj4 = ['A','B','C']
        obj5 = [59]
        ol.insert(self.obj1)
        
        ol.insert(self.obj2)
        ol.insert(self.obj4)
        ol.insert(self.obj5)
        obj3 = self.ol.find(self.obj1)
        
        



    Insert method:
      inserts an item into the ordered list
            items are inserted at the end of the list, which is determined by the count
            attribute
            
            Args:
                `obj` : item to be inserted
            Raises:
            -------
                `ContainerFull` exception
                
    withdraw method:
      withdraws `obj` from the `OrderedList`
            
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
   Cursor:
    An abstraction of position in an OrderedList instance
        
            Extends:
            --------
            `Cursor`
            Attributes:
            -----------
                _list : `OrderedListAsArray` instance
                _offset : `int`  records an offset in the _list array of objects
  insert `obj` after the current Cursor position
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
    Cursor.insertBefore
      insert `obj` before the current Cursor position
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
OrderedListAsArray.findPosition :
  Finds the position of `obj` in the `OrderedList`
        
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

   


