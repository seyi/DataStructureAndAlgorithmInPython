'''
Created on May 27, 2019

@author: anointedone
'''
from time import time
class ACostCalc(object):
    '''
    classdocs
    '''


    def __init__(self, n):
        '''
        Constructor
        '''
        self._n = n

    def compute_average(self):
        """Perform n appends to an empty list and return average time elapsed """
        data = []
        start = time()
        for k in range(self._n):
            data.append(None)
        end = time()
        return (end - start )/ self._n

    def getN(self):
        return self._n
    def setN(self,n):
        self._n = n

    n = property(
                 fget = lambda self: self.getN())


