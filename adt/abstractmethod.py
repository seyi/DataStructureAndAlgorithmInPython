'''
Created on May 25, 2019

@author: anointedone
'''
import inspect

class abstractmethod(object):
    '''
    classdocs
    '''


    def __init__(self, func):
        '''
        Constructor
        '''
        assert inspect.isfunction(func)
        self._func = func

    def __get__(self,obj,type):
        return self.method(obj,self._func,type)

    class method(object):

        def __init__(self,obj,func,cls):
            self._self = obj
            self._func = func
            self._class = cls
            self.__name__ = func.__name__

        def __call__(self,*args,**kwargs):
            msg = "Abstract method %s of class %s called. " %(
                        self._func.__name__,self._class.__name__)
            raise TypeError(msg)