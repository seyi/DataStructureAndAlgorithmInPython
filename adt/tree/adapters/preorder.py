'''
Created on 17 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.tree.prepostvisitor import PrepostVisitor

class PreOrder(PrepostVisitor):
    ''' adapter class that provides a mapping to the `preVisit` interface
    
        Notes:
            Provides interface for visitor (`Visitor`) instance that do not conform
            to the `PrepostVisitor.preVisit` interface
    
    '''

    def __init__(self, visitor):
        '''
        Constructor
        '''
        self._visitor = visitor
        
    def preVisit(self,obj):
        self._visitor.visit(obj)
    
    def getIsDone(self):
        self._visitor.isDone
        