'''
Created on 9 Jun 2019

@author: anointedone
'''
from adt.visitor import Visitor
class MatchVisitor(Visitor):
    '''
    Derived visitor
    '''


    def __init__(self,target):
        '''
        Constructor
        '''
        super(MatchVisitor, self).__init__()
        self._target = target
        self._found = None
        
    def visit(self,obj):
        if not self.isDone() and obj == self._target:
            if self._target == None:
                self._found = 'None as target'
            else:
                self._found = obj
            print('found %s'%self._target )
            
    def isDone(self):
        return self._found is not None
        
        