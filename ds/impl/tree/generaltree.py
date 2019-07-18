'''
Created on 9 Jul 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.tree.tree import Tree
from datastructureandalgorithminpython.adt.l_list import LinkedList
from collections import Iterable
from datastructureandalgorithminpython.adt.tree.prepostvisitor import PrepostVisitor


class GeneralTree(Tree):
    '''
    classdocs
    '''


    def __init__(self, key):
        '''
        Constructor
        '''
        super(GeneralTree, self).__init__()
        self._key = key
        self._degree = 0
        self._count  = 0
        self._list = LinkedList()
        
    def purge(self):
        self._list.purge()
        self._degree = 0
    
    def getKey(self):
        return self._key
    
    def getSubTree(self,i):
        if i < 0 or i >= self._degree:
            raise IndexError
        ptr = self._list.head
        
        for j in range(i):
            ptr = ptr._next
            
        return ptr.datum
    
    def attachSubtree(self,tree):
        self._list.append(tree)
        self._degree += 1
        self._count += 1
        
        
    def detachSubtree(self,tree):
        try:
            self._list.extract(tree)
            self._degree -= 1
            self._count -= 1
        except KeyError:
            return None
        else:
            return tree
        
    def depthFirstTraversal(self, visitor):
        assert(isinstance(visitor, PrepostVisitor))
        if self._degree > 0:
            visitor.preVisit(self._key)
            visitor.inVisit(self._key)
            for i in range(self._degree):
                self.getSubTree(i).depthFirstTraversal(visitor)   
            visitor.postVisit(self._key)
        else:
            visitor.preVisit(self._key)
            visitor.inVisit(self._key)
            visitor.postVisit(self._key)
        
    def __str__(self,*args,**kwargs):
        v = GeneralTree.PrintVisitor()
        self.depthFirstTraversal(v)
        return str(v)
    
    def previsit(self,visitor,obj):
        visitor.s = visitor.s+str(obj)
        
    class PrintVisitor(PrepostVisitor):
        
        def __init__(self):
            super(GeneralTree.PrintVisitor, self).__init__()
            self._s = ''
            
        def preVisit(self, obj):
            self._s = self._s+' {'
        def inVisit(self, obj):
            self._s = self._s + str(obj)
        def postVisit(self, obj):
            self._s = self._s+'}'
            
        def __str__(self,*args,**kwargs):
            #return ''.join(str(x) for x in self._s)
            return self._s
                
        
                 
        
        
    
        
                
   
    #===========================================================================
    #     res = []
    #     
    #     for t in self._list:
    #         if t._datum is Iterable:
    #             self.__str__(t._datum)
    #         else:
    #             res.append({type(t):t._datum})
    #             
    #     return res
    # 
    #===========================================================================
        
        