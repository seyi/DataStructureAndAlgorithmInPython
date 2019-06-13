'''
Created on 12 Jun 2019

@author: anointedone
'''
from adt.abstractmethod import abstractmethod

class Cursor(object):
    '''An abstract cursor class
        Notes:
        ------
        A cursor remembers the position of an item in a list
    
    '''


    def __init__(self,mlist):
        '''
        Constructor
        '''
        self._list = mlist
        
    def getDatum(self):
        pass
    getDatum = abstractmethod(getDatum)
    datum = property(
        fget = lambda self: self.getDatum())
    
    def insertAfter(self,obj):
        pass
    insertAfter = abstractmethod(insertAfter)
    
    def insertBefore(self,obj):
        pass
    iinsertBefore = abstractmethod(insertBefore)
    
    def withdraw(self,obj):
        pass
    withdraw = abstractmethod(withdraw)
        