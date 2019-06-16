'''
Created on 6 Jun 2019

@author: anointedone
'''

class Association(object):
    '''
    An ordered pair of objects
    the first element of the object is called the key
    The second element is called the value
    '''
    def __init__(self, *args):
        '''
        Constructor
        '''
        if len(args) == 1:
            self._tuple = (args[0],None)
        elif len(args) == 2:
            self._tuple = args
        else:
            raise ValueError
        
        #=======================================================================
        # properties
        #=======================================================================
        
        def getKey(self):
            """ 
                Returns the value of the first element of the tuple
            """
            return self._tuple[0]
        key = property(
            fget = lambda self: self.getKey())
        def getValue(self):
            return self._tuple[1]
        value = property(
            fget = lambda self : self.getValue())
        
        
        
        #=======================================================================
        # Methods
        #=======================================================================
        def _compareTo(self,assoc):
            """ Compares association with an instance of the 
                association class.
                Assocation comparison is based solely on the keys and not the value
                
            """
            assert(isinstance(self,assoc.__class__))
            return cmp(self.key,assoc.key)
        
        def __str__(self):
            """ A textual representation of the association class"""
            return "Association %s " % str(self._tuple)
        
        def __hash__(self):
            return hash(self.key)
            
            