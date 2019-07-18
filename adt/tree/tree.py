'''
Created on 17 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.Container import Container
from datastructureandalgorithminpython.adt.abstractmethod import abstractmethod
from .prepostvisitor import PrepostVisitor
from datastructureandalgorithminpython.adt.visitor import Visitor
from datastructureandalgorithminpython.ds.impl.queueaslinkedlist import QueueAslinkedList
from datastructureandalgorithminpython.adt.tree.adapters.preorder import PreOrder
from datastructureandalgorithminpython.adt.it import Iterator
from datastructureandalgorithminpython.ds.impl.stackaslinkedlist import StackAsLinkedList

class Tree(Container):
    '''
    classdocs
    '''

    def getKey(self):
        pass
    key = abstractmethod(getKey)
    
    def getSubTree(self):
        pass
    getSubTree = abstractmethod(getSubTree)
    
    def getIsLeaf(self):
        pass
    getIsLeaf = abstractmethod(getIsLeaf)
    
    isLeaf = property(
        fget = lambda self: self.getIsLeaf())
    
    def getDegree(self):
        pass
    getDegree = abstractmethod(getDegree)
    degree = property(
        fget = lambda self : self.getDegree())
    
    def getHeight(self):
        pass
    height = property(
        fget = lambda self: self.getDegree())
    
    
    def depthFirstTraversal(self,visitor):
        """An abstract algorithm which describes the the depthFirstTraversal
           behaviour in the absence of an implementation 
            Notes:
            ------
                Firstly, the visitor is checked to assert if it an instance of
                the `PrePostVisitor` class. This technique helps enforce proto-
                cols.
                The preVisit method of the visitor is then called with the
                key property of the tree (`self.key`).
                
                The next phase of the algorithm is an iterative process where 
                the range is determined by degree (`self.degree`) of the tree.
                During the process an instance of the subtree is acquired based
                on the index of the current range (`self.getSubtree(i)`) and the 
                `depthFirstTraversal` method of the instance is called passing
                in the `visitor` as argument
                
                Finally the `postVisit` visitor method is called with the tree 
                key property as argument
        """
        assert(isinstance(visitor, PrepostVisitor))
        if not self.isEmpty and not visitor.isDone():
            visitor.preVisit(self.key)
            for i in range(self.degree):
                self.getSubTree(i).depthFirstTraversal(visitor)
            visitor.postVisit(self.key)
            
    def breadthFirstTraversal(self,visitor):
        assert(isinstance(visitor, Visitor))
        queue = QueueAslinkedList()
        if not self.isEmpty:
            queue.enqueue(self)
        while not queue.isEmpty and not visitor.isDone:
            head = queue.dequeue()
            visitor.visit(head.key)
            for i in range(head.degree):
                child = head.getSubTree(i)
                if not child.isEmpty:
                    queue.enqueue(child)
                    
    def accept(self,visitor):
        assert(isinstance(visitor, Visitor))
        self.depthFirstTraversal(PreOrder(visitor))
        
    class Iterator(Iterator):
        
        def __init__(self, tree):
            super(Tree.Iterator, self).__init__(tree)
            self._stack = StackAsLinkedList()
            if not tree.isEmpty:
                self._stack.push(tree)
            
        def next(self):
            if not self._stack.isEmpty:
                top = self._stack.pop()
                i = top.degree - 1
                while i >= 0 :
                    subtree = top.getSubTree(i)
                    if not subtree.isEmpty:
                        self._stack.push(subtree)
                    i -= 1
                return top.key
            else:
                raise StopIteration
    def __iter__(self):
        return Tree.Iterator(self)
            
            
            
        