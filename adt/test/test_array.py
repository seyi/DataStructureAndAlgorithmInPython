'''
Created on May 29, 2019

@author: anointedone
'''
import unittest
from adt.array import Array



class Test(unittest.TestCase):


    def setUp(self):
        self._arr = Array(4)
        for i in range(len(self._arr)-1):
            self._arr[i] = i
            


    def tearDown(self):
        pass


    def testName(self):
        pass
    def testgetitem(self):
        self.assertEqual(self._arr[2],1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()