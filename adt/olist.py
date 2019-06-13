'''
Created on 12 Jun 2019

@author: anointedone
'''
from adt.searchablecontainer import SearchableContainer
from adt.abstractmethod import abstractmethod
from datastructureandalgorithminpython.position.cursor import Cursor

class OrderedList(SearchableContainer):
    '''An Abstract Base class for Ordered List
    
        ParentClass:
        -----------
            `SearchableContainer`
        
        
        Notes:
        -----
        An ordered list is a container in which the order of the items
        is significant.However the items in an Ordered list are not necesarily sorted
        
        As a result of the unsorted property, it is possible to make
        insertions which changes the order of the items in an OrderedList
        
        
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(OrderedList, self).__init__()
        
    def __getitem__(self,idx):
        pass
    __getitem__ = abstractmethod(__getitem__)
    
    def findPosition(self,obj):
        """ Searches the list for `obj` and return the position
        
            Returns:
            --------
             `Cursor` 
        
        """
        pass
    findPosition = abstractmethod(findPosition)
        