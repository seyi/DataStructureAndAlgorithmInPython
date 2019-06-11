'''
Created on 3 Jun 2019

@author: anointedone
'''
import unittest
from adt.dmat import Matrix


class Test(unittest.TestCase):


    def setUp(self):
        self._m = Matrix(2,2)


    def tearDown(self):
        pass


    def testInit(self):
        m = Matrix(1,2)
        
    def testNumRows(self):
        self.assertEqual(self._m.getNumberOfRows(), 2)
        
    def testNumCol(self):
        self.assertEqual(self._m.getNumberOfColumns(), 2 )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()