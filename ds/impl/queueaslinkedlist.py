'''
Created on 10 Jun 2019

@author: anointedone
'''
from adt.queue import Queue
from adt.l_list import LinkedList
from adt.exceptions.exceptions import ContainerEmpty, ContainerFull
class QueueAslinkedList(Queue):
    
    '''
    classdocs
    '''


    def __init__(self, size=0):
        '''
        Constructor
        '''
        def __init__(self):
            super(QueueAslinkedList, self).__init__()
            self._list = LinkedList()
            
            
        def purge(self):
            if self._count == 0:
                raise ContainerEmpty
            self._list.purge()
            self._count = 0
        def getHead(self):
            if self._count == 0:
                raise ContainerEmpty
            return self._list.getFirst()
        def enqueue(self, item):
            self._list.append(item)
            self._count += 1
        
            
        def dequeue(self):
            if self._count == 0:
                raise ContainerEmpty
            result = self._list.getFirst()
            self._list.extract(result)
            self._count -= 1
            return result
            
            
            