'''
Created on 15 Jun 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.ds.impl.orderedlistaslnkedlist import OrderedListAsLinkedList


class Test(unittest.TestCase):


    def setUp(self):
        self.ol = OrderedListAsLinkedList()
        self.ol.insert(1)
        self.ol.insert(2)
        self.ol.insert(3)
        for i in range(4,100):
            self.ol.insert(i)


    def tearDown(self):
        pass


    def testInsert(self):
        self.assertEquals(self.ol._linkedlist.getLast().getDatum(),99)
    def testgetitem(self):
        self.assertEqual(self.ol[67],68)
        
    def testcontains(self):
        self.assertTrue(37 in self.ol)
        
    def testfind(self):
        self.assertEqual(self.ol.find(50),50)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInsert']
    unittest.main()