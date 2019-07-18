'''
Created on 4 Jun 2019

@author: anointedone
'''

from adt.exceptions.exceptions import ContainerEmpty
from datastructureandalgorithminpython.adt.it import Iterator



class LinkedList(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self._head = None
        self._tail = None
        
    def purge(self):
        self._head = None
        self._tail = None
        
    #===========================================================================
    # properties
    #===========================================================================
    def getHead(self):
        return self._head
    head = property(
        fget = lambda self : self.getHead())
    def getTail(self):
        return self._tail
    tail = property(
        fget = lambda self : self.getTail())
    def getIsEmpty(self):
        return self._head is None
    isEmpty = property(
        fget = lambda self : self.getIsEmpty())
    def getFirst(self):
        """ Get the first element in the list """
        if self._head is None:
            raise ContainerEmpty
        return self._head._datum
    first = property(
        fget = lambda self : self.getFirst())
    def getLast(self):
        """ Returns the last element in the linked list """
        if self._tail is None:
            raise ContainerEmpty("The list element is empty")
        return self._tail 
    last = property(
        fget =  lambda self : self.getLast())
    
    def prepend(self,item):
        """ Add an item to the front of the linked list"""
        tmp = self.Element(self,item,self._head)
        if self._head is None:
            self._tail = tmp
        self._head = tmp
        
    def append(self,item):
        tmp = self.Element(self,item,None)
        if self._head is None:
            self._head = tmp
        else:
            self._tail._next = tmp
            
        self._tail = tmp
        
    
    def extract(self,item):
        """ extracts item from the linkedlist, by replacing the element that contains item
            with the next element, if item is found in the head, with the previous element if not the head,
            or replacing the tail with the previous element if found at the tail 
        """
        ptr = self._head
        prevPtr = None
        while ptr is not None and ptr._datum is not item:
            prevPtr = ptr
            
            ptr = ptr._next
            #assert(prevPtr != ptr) , prevPtr.__dict__.__str__() + ' == ' + ptr.__dict__.__str__()
            #print('PPAfter ptr._next modification: '+prevPtr.__dict__.__str__())
            
            
        if ptr is None:
            raise KeyError
        if ptr == self._head:
            self._head = ptr._next
        else:
            prevPtr._next = ptr._next
            
        if ptr == self._tail:
            self._tail = prevPtr     
        
        
    def __copy__(self):
        """ Creates a shallow copy of the LinkedList"""
        #result = LinkedList()
        #ptr = self._head
        #while ptr is not None:
            #result.append(ptr._datum)
            #ptr = ptr._next
        #return result
        pass
            
    
    class Element(object):
        def __init__(self,m_list,datum,m_next):
            self._list = m_list
            self._datum = datum
            self._next = m_next
            
        def getDatum(self):
            return self._datum
        datum = property(
            fget = lambda self: self.getDatum())
        def getNext(self):
            return self._next
        next = property(
            fget = lambda self: self.getNext())
        
        def insertAfter(self,item):
            self._next = LinkedList.Element(
                self._list,item,self._next)
            if self._list._tail is self:
                self._list._tail = self._next
                
        def insertBefore(self,item):
            tmp = LinkedList.Element(self._list,item,self)
            if self is self._list._head:
                self._list._head = tmp
            else:
                prevPtr = self._list._head
                while prevPtr is not None and prevPtr._next is not self:
                    prevPtr = prevPtr._next
                    prevPtr._next = tmp
                    
    class Iterator(Iterator):
        
        def __init__(self,list):
            super(Iterator, self).__init__()
            self._ptr = list.getHead()
            
        def next(self):
            if self._ptr is None:
                raise StopIteration
            else:
                
                item = self._ptr._datum
                self._ptr = self._ptr._next
                return item
            
    def __iter__(self):
        return LinkedList.Iterator(self)
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.append("Hello")
    ll.append("World")
    
    it = iter(ll)
    
    while True:
        try:
            print(next(it))
        except StopIteration:
            break     
        
        
            