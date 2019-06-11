
from adt.abstractmethod import abstractmethod


class Iterator(object):
    """ An Iterator provides the means to access one-by-one the objects
        in a Container.
        A python iterator provides two methods called __iter__
        and next or __next__ and that implement the Iterator protocol
        below.
        
        The idea is that for every derived class from the Container
        base class, we also implement a related Iterator class
        derived from the abstract Iterator class 
    """ 
    
    def __init__(self,container):
        #super(object, self).__init__()
        self._container = container
        
    def __iter__(self):
        return self
    def next(self):
        """ Derived classes are meant to implement this protocol"""
        pass
    
    next = abstractmethod(next)
        