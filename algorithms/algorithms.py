'''
Created on 8 Jul 2019

@author: anointedone
'''
from datastructureandalgorithminpython.ds.impl.queueaslinkedlist import QueueAslinkedList

class Algorithms(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod    
    def breadthfirst(tree):
        queue = QueueAslinkedList()
        queue.enqueue(tree)
        
        while not queue.isEmpty():
            t = queue.dequeue()
            print(t.key)
            
            for i in range(t.degree):
                subtree = t.getSubTree(i)
                queue.enqueue(subtree)
        