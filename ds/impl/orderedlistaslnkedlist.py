'''
Created on 15 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.olist import OrderedList
from datastructureandalgorithminpython.adt.l_list import LinkedList
from datastructureandalgorithminpython.adt.exceptions.exceptions import ContainerEmpty
from __builtin__ import False

class OrderedListAsLinkedList(OrderedList):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OrderedListAsLinkedList, self).__init__()
        self._linkedlist = LinkedList()
        
    def insert(self, obj):
        self._linkedlist.append(obj)
        self._count += 1
        
    def __getitem__(self, idx):
        if idx < 0 or idx >= self._count:
            raise IndexError
        ptr = self._linkedlist.getHead();
        i = 0
        
        while i < idx and ptr is not None:
            ptr = ptr.next
            i += 1
        
        return ptr._datum
    
    def __contains__(self, obj):
        if self._count == 0:
            raise ContainerEmpty
        ptr = self._linkedlist.getHead()
        
        while ptr is not None and ptr._datum is not obj:
            ptr = ptr._next
        if ptr is None:
            return False
        return True
    
    def find(self, obj):
        if self._linkedlist.isEmpty:
            raise ContainerEmpty()
        ptr = self._linkedlist.getHead()
        while ptr is not None and ptr._datum != obj:
            ptr = ptr.next
        if ptr is None:
            raise KeyError
        return ptr._datum
            