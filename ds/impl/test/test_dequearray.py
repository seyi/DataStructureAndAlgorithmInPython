'''
Created on 11 Jun 2019

@author: anointedone
'''
import unittest
from ds.impl.dequeasarray import DequeAsArray

class TestDequeArray(unittest.TestCase):
    
    def setUp(self):
        self._da = DequeAsArray(5)
        self._da.enqueue('the')
        self._da.enqueue('quick')
        self._da.enqueue('brown')
        self._da.enqueue('fox')
    def testEnqueueHead(self):
        da = DequeAsArray(5)
        da.enqueueHead('the')
        self.assertEquals(da.getHead(), 'the')
        da.enqueueHead('quick')
        self.assertEquals(da.getHead(), 'quick')
    def testEnqueueDequeueHeadTail(self):
            self.assertEquals(self._da.dequeue(),'the')
            self.assertEquals(self._da.dequeueTail(),'fox')
            self.assertEquals(self._da.dequeue(),'quick')
            self._da.enqueueHead('hugaga')
            self._da.enqueueHead('balaga')
            self.assertEquals(self._da.dequeue(),'balaga')
            self.assertEquals(self._da.dequeue(),'hugaga')
            self._da.enqueue('ogbeni')
            self.assertEquals(self._da.dequeueTail(),'ogbeni')
            
            
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEnqueue']
    unittest.main()

    