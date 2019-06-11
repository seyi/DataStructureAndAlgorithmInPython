'''
Created on 6 Jun 2019

@author: anointedone
'''
from adt.abstractmethod import abstractmethod

class SearchableContainer(object):
    '''
    An extension of the container abstraction
    Adds methods to search a container for a given object
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        def __init__(self):
            super(SearchableContainer,self).__init__()
            
        def __contains__(self,obj):
            pass
        __contains__ = abstractmethod(__contains__)
        def insert(self,obj):
            pass
        insert = abstractmethod(insert)
        
        def withdraw(self,obj):
            pass
        withdraw = abstractmethod(withdraw)
        
        def find(self,obj):
            pass
        find = abstractmethod(find)
        
        
        