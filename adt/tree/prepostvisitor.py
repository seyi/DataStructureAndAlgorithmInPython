'''
Created on 17 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.visitor import Visitor
from datastructureandalgorithminpython.adt.abstractmethod import abstractmethod

class PrepostVisitor(Visitor):
    ''' A visitor with three methods,preVisit, inVisit and postVisit
        
        Notes:
        ------
            The preVisit and the postVist methods are called durring a
            depth-first-traversal of the tree
            
            The preVisit method carries out a preOrder traversal, a 
            type of DepthFirstTraversal starting at the
            root of the tree, then recursively traverse the left subtree accord-
            to the depth , before going to the right of the  tree, carrying out
            the same process
            
            The postVisit interface facilitates a postOrder tree traversal, which
            is characterised by traversing the left subtree first according to -
            degree, before traversing the right subtree , then finally the root
            
            for example, given a tree,
            T = {A,{B,None,{C,None,None}},{D,{E,{F,None,None},{G,None,None}},{H,{I,None.None},None}}}
            postOrder traversal starts follows the order CBFGEIHDA
            
            The inVisit interface performa a depth first type of traversal that 
            visits the left subtree, starting at the lowest leaf node at the 
            left, moves right, then upwards starting at the left node, visits
            the root before moving on to the right subtree, starting at the left 
            leaf of the lowest node
            
        Extends:
            `Visitor`
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(PrepostVisitor, self).__init__()
        
    def preVisit(self,obj):
        pass
    preVisit = abstractmethod(preVisit)
    
    def inVisit(self,obj):
        pass
    inVisit = abstractmethod(inVisit) 
    
    def postVisit(self,obj):
        pass
    postVisit = abstractmethod(postVisit)
    
    visit = inVisit()
        