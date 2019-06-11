'''
Created on 3 Jun 2019

@author: anointedone
'''
import unittest
from adt.dmat import DenseMatrix


class Test(unittest.TestCase):
    def setUp(self):
        self._dm = DenseMatrix(2,3)
        for i in range(len(self._dm._array.getData())-1):
            self._dm._array.getData()[i] = i+1


    def tearDown(self):
        pass

    def testGetItem(self):
        self.assertEqual(self._dm[1,1],90)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetItem']
    unittest.main()
    