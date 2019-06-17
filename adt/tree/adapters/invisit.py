'''
Created on 17 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.tree.prepostvisitor import PrepostVisitor

class InVisit(PrepostVisitor):
    ''' adapter class that provides a mapping to the `inVisit` interface
    
        Notes:
            Provides interface for visitor (`Visitor`) instance that do not conform
            to the `PrepostVisitor.inVisit` interface
    
    '''
    def __init__(self, visitor):
        '''
        Constructor
        '''
        super(InVisit, self).__init__()
        self._visitor = visitor
        
    def inVisit(self, obj):
        self._visitor.visit(obj)
    def getIsDone(self):
        self._visitor.isDone