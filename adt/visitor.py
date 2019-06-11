'''
Created on 6 Jun 2019

@author: anointedone
'''

class Visitor(object):
    """ Base class for visitor
        provides one by one access to elements in a container
        and performs an operation on the visited element
    """
    
    def __init__(self):
        super(Visitor,self).__init__()
        
    def visit(self):
        pass
    def getIsDone(self):
        return False
    isDone = property(
        fget = lambda self: self.getIsDone())