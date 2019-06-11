'''
Created on May 29, 2019

@author: anointedone
'''
import unittest

from adt.mda import MultiDimensionalArray
class Test(unittest.TestCase):


    def setUp(self):
        self._mda = MultiDimensionalArray(5,2,2)
        for i in range(len(self._mda.data)):
            self._mda.data[i] = i+1
                    
    def tearDown(self):
        pass


    def testInit(self):
        self.assertEqual(len(self._mda._data._data), 20)
        self.assertEqual(self._mda._dimensions[1],2)
        self.assertEqual(len(self._mda._factors.data),3)

    def testGetOffset(self):
        self.assertEqual(self._mda.getOffset((0,0,1)), 1)
    def testGetItem(self):
        self.assertEqual(self._mda[1,0,0], 4)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    s = frozenset([1,2,3])