'''
Created on 15 Jun 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.ds.impl.sortedlistasarray import SortedListAsArray


class Test(unittest.TestCase):


    def setUp(self):
        self.sl = SortedListAsArray(500)
        self.sl.insert(2)
        self.sl.insert(1)
        self.sl.insert(4)
        self.sl.insert(7)
        for i in range(8,100):
            self.sl.insert(i)
        


    def tearDown(self):
        pass


    def testIsSorted(self):
        for i,obj in enumerate(self.sl):
            if i == self.sl._count-1:
                return
            self.assertTrue(self.sl[i] < self.sl[i+1])
    def testFindOffset(self):
        self.assertEqual(self.sl.findOffset(94), 90)
        
    def testFind(self):
        self.assertEqual(self.sl.find(80),80)
        self.assertEqual(self.sl.find(8000),None)
        
    def testfindposition(self):
        self.assertEqual(self.sl.findPosition(50)._offset,100)
        
    def testwithdraw(self):
        self.sl.withdraw(50);
        self.assertEqual(self.sl.findOffset(50),-1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInsert']
    unittest.main()