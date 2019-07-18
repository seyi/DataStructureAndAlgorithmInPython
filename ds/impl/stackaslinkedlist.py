'''
Created on 9 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.l_list import LinkedList
from datastructureandalgorithminpython.adt.exceptions.exceptions import ContainerEmpty
from datastructureandalgorithminpython.adt.visitor import Visitor
from datastructureandalgorithminpython.adt.it import Iterator
from datastructureandalgorithminpython.adt.stack import Stack

class StackAsLinkedList(Stack):
    '''
    Stack that makes use of the LinkedList datastructure
    '''


    def __init__(self):
        '''
        With a Linked List, there is no need to preallocate storage space
        Storage space is added as needed in a dynamic fashion
        The init method creates an empty LinkedList an assignss it to the
        _list attribute
        '''
        
        super(StackAsLinkedList, self).__init__()
        self._list = LinkedList()
        
    def purge(self):
        self._list.purge()
        
    #===========================================================================
    # Push, pop and get methods
    #===========================================================================
    
    def push(self,obj):
        self._list.prepend(obj)
        self._count += 1
        
    def pop(self):
        if self._count == 0 :
            raise ContainerEmpty
        result = self._list.getFirst()
        self._list.extract(result)
        self._count -= 1
        return result
    def getTop(self):
        if self._list.isEmpty:
            raise ContainerEmpty()
        return self._list.first
    
    def accept(self,visitor):
        assert(isinstance(visitor, Visitor))
       
        ptr = self._list.getHead()
        print("list head %s"%ptr.__dict__.__str__())
        while ptr is not None:
            print("Visitor visiting %s"%ptr.__dict__.__str__())
            visitor.visit(ptr.getDatum())
            if visitor.isDone() == True:
                print("visitor is done at %s"%ptr.__dict__.__str__())
                return  
            ptr = ptr.getNext()
            
    class Iterator(Iterator):
        def __init__(self, stack):
            super(Iterator, self).__init__(stack)
            self._position = stack._list.head
            
        def next(self):
            if self._position is None:
                raise StopIteration
            element = self._position
            self._position = self._position.next
            return element.datum
        
        def __iter__(self):
            return self.Iterator(self)
            
        
        