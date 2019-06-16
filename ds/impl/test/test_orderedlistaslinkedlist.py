'''
Created on 15 Jun 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.ds.impl.orderedlistaslnkedlist import OrderedListAsLinkedList
from datastructureandalgorithminpython.adt.l_list import LinkedList

class Test(unittest.TestCase):


    def setUp(self):
        self.ol = OrderedListAsLinkedList()
        self.ol.insert(1)
        self.ol.insert(2)
        self.ol.insert(3)
        for i in range(4,100):
            self.ol.insert(i)
        self.ol.insert({'a':1, 'b':9})


    def tearDown(self):
        pass


    def testInsert(self):
        self.assertEquals(self.ol._linkedlist.getLast().getDatum(),{'a':1, 'b':9})
    def testgetitem(self):
        self.assertEqual(self.ol[67],68)
        
    def testcontains(self):
        self.assertTrue(37 in self.ol)
        
    def testfind(self):
        self.assertEqual(self.ol.find(50),50)
        
    def testFindPosition(self):
        self.assertEqual(dict({'a':1, 'b':9}),self.ol.findPosition({'a':1, 'b':9}).getDatum())
        
    def testInsertAfter(self):
        c = self.ol.findPosition({'a':1, 'b':9})
        c.insertAfter((1,2,3,4))
        self.assertEqual(self.ol.findPosition((1,2,3,4)).getDatum(),c._element._next._datum)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInsert']
    unittest.main()