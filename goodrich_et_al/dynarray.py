'''
Created on May 27, 2019

@author: anointedone
'''
import ctypes
class DynamicArray(object):
    ''' A dynamic array akin to a simplified python list
    classdocs
    '''


    def __init__(self):
        '''
        Create an empty array
        '''
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def len(self):
        """ Return number of elements stored in the array """
        return self._n

    def __getitem__(self,k):
        """ Return element at index k """
        if not 0 <= k < self._n :
            raise IndexError('Invalid index')
        return self._A[k]
    def append(self,obj):
        """ add obkect to the end of array """
        if self._n == self._capacity :
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self,c):
        ''' Resize internal array to capacity c '''
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        """ return new array with capacity c """
        return (c * ctypes.py_object)()
    def insert(self,k,value):
        ''' insert value at index k , shifting subsequent values rightwards'''
        if self._n == self._capacity :
            self._resize(2*self._capacity)

        for j in range(self._n,k,-1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self,value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k,self._n-1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n -1] = None
                self._n -= 1
                return

        raise ValueError('Value not found')

    def insertR(self,new,old):
        for k in range(self._n):
            if self._A[k] == old :
                self.insert(k+1, new)
                return
        raise ValueError('value not found')




