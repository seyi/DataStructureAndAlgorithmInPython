'''
Created on 4 Jun 2019

@author: anointedone
'''

class ContainerEmpty(Exception):
    """ The container object is empty """
    pass

class ContainerFull(Exception):
    """ The Container object is full"""
    pass
class StateError(Exception):
    """ Invalid State encountered"""
class IllegalArgumentError(Exception):
    """ Illegal argument"""