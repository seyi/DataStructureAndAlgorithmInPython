'''
Created on 17 Jun 2019

@author: anointedone
'''
from datastructureandalgorithminpython.adt.tree.prepostvisitor import PrepostVisitor

class PostOrder(PrepostVisitor):
    '''
    classdocs
    '''


    def __init__(self, visitor):
        '''
        Constructor
        '''
        super(PostOrder, self).__init__()
        self._visitor = visitor
    def postVisit(self, obj):
        self._visitor.visit(obj)
        
    def getIsDone(self):
        self._visitor.isDone