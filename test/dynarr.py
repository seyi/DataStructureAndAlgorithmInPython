'''
Created on May 28, 2019

@author: anointedone
'''
import unittest
from goodrich_et_al.dynarray import DynamicArray

class DynArrayTest(unittest.TestCase):

    dynArr = property(fget = lambda self : DynamicArray())
    def setUp(self):
        self._dynArr = DynamicArray()
        self._dynArr.append(1)
        self._dynArr.append(2)
        self._dynArr.append(3)
        self._dynArr.append(2)



    def tearDown(self):
        pass


    def Remove(self):
        self._dynArr.remove(2)
        self.assertEqual(self._dynArr[1], 3,
                          'Unequal array')
        self.assertEqual(self._dynArr[2], 4,
                          'Unequal array')
        #self.assertEqual(self.dynArr._n, 4,
         #                 'Unequal array')
    def insertR(self,new,old):
        for k in range(self._dynArr._n):
            if self._dynArr._A[k] == old :
                self._dynArr.insert(k+1, new)
                return
        raise ValueError('value not found')

    def testInsertR(self):
        self._dynArr.insertR(10, 2)
        self.assertEqual(self._dynArr._n, 5)
        self.assertEqual(self._dynArr._A[0], 1)
        self.assertEqual(self._dynArr._A[1], 2)
        self.assertEqual(self._dynArr._A[2], 10)
        self.assertEqual(self._dynArr._A[3], 3)
        self.assertEqual(self._dynArr._A[4], 2)





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()