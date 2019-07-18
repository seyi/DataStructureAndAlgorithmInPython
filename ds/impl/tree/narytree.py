'''
Created on 18 Jul 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.tree.tree import Tree
from datastructureandalgorithminpython.adt.array import Array
from datastructureandalgorithminpython.adt.exceptions.exceptions import StateError,\
    IllegalArgumentError
from datastructureandalgorithminpython.adt.visitor import Visitor
from datastructureandalgorithminpython.adt.tree.prepostvisitor import PrepostVisitor



class NaryTree(Tree):
    '''
        A Nary tree is either a tree with an empty node or a tree 
        comprised of a root with exactly N subtrees
        
        Notes:
        ------
        Representation in memory:The Nary tree has elements stored in 
        array of N length, with each element as pointers to either another
        tree or an empty node as in {A, {B, {None}, {None},{None}},{None},{None}}
        The empty trees indicated with none are explicitly represented as
        trees rather than leaf nodes and contain neither roots nor subtrees
    '''


    def __init__(self, *args):
        '''
            Init of the Nary tree is based on the `args` tuple
            the first element of the tuple is used to initialize the degree,
            while the second element initializes the key (`self._key`).
            
            Subtree initialization depends on the presence of the second element
            in `args` where an array is used for each degree of the subtree
        '''
        super(NaryTree, self).__init__()
        
        if len(args) == 1:
            self._degree = args[0]
            self._key = None
            self._subtree = None
        elif len(args) == 2:
            self._degree = args[0]
            self._key  = args[1]
            self._subtree = Array(self._degree)
            for i in range(self._degree):
                self._subtree[i] = NaryTree(self._degree)
        else:
            raise IllegalArgumentError
                
    def purge(self):
        self._key = None
        self._degree = None
        
    def getIsEmpty(self):
        return self._key is None
    
    def getKey(self):
        """ Returns key
            Exception:
            ----------
                `StateError` if attempt is made to get the key of an empty tree       
        """
        if self.isEmpty:
            raise StateError
        return self._key
    
    def attachKey(self,obj):
        """ attaches `obj` as key for tree
            Attachment is permitted only on empty trees , hence a StateError
            is raised if an attempt is made to update a Nary tree's key
            
            Since this operation is on empty trees, subtrees are created
            by iterating on the degree of the tree   
        """
        if not self.isEmpty:
            raise StateError
        self._key = obj
        self._subtree = Array(self._degree)
        for i in range(self._degree):
            self._subtree[i] = NaryTree(self._degree)
            
    def detachKey(self):
        """ Detaches a  Narytree key.Method is only permmited on leaf nodes
            
            Raises:
            -------
                `StateError` for non leaf elements
                
            Returns:
                key
            
            Notes:
            ------
                After a successful detachment, the key and subtree attributes
                are set to None        
        """
        if not self.isLeaf:
            raise StateError
        result = self._key
        
        self._key = None
        self._subtree = None
        return result
    
    class PrintVisitor(PrepostVisitor):
        
        def __init__(self):
            super(NaryTree.PrintVisitor, self).__init__()
            self._s = ''
        def preVisit(self, obj):
            self._s = self._s + '{'
        def inVisit(self, obj):
            self._s = self._s + str(obj)# if not obj is None else  self._s + 'None'
        def postVisit(self, obj):
            self._s = self._s + '}'
            
        def __str__(self):
            return self._s
            
    def depthFirstTraversal(self, visitor):
        visitor.preVisit(self._key)
        visitor.inVisit(self._key)
        for i in range(self._degree): 
            if not self._subtree is None:
                self._subtree[i].depthFirstTraversal(visitor)   
        visitor.postVisit(self._key)
        
    def __str__(self):
        visitor  = NaryTree.PrintVisitor()
        #visitor.preVisit(self._key)
        #visitor.inVisit(self._key)
        self.depthFirstTraversal(visitor)
        #visitor.postVisit(self._key)
        
        return str(visitor)
        
        
        