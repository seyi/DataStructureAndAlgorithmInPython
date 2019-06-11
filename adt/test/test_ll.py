'''
Created on 5 Jun 2019

@author: anointedone
'''
import unittest
from adt.l_list import LinkedList


class Test(unittest.TestCase):


    def setUp(self):
        self.ll = LinkedList()
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)


    def tearDown(self):
        pass


    def testHead(self):
        self.assertEqual(self.ll.getHead()._datum, 1)
    
    def testGetTail(self):
        self.assertEqual(self.ll.getTail()._datum, 4)
    
    def testNext(self):
        self.assertEqual(self.ll.getHead().getNext().getNext().getNext(), self.ll.getTail())
        ll2 = LinkedList();
        ll2.append(1)
        #self.assertIsNone(ll2.getHead().getNext())
        #ll2.append(2)
        ll2._tail._next = LinkedList().Element(ll2,56,None)
        ll2._tail._datum = "the quick brown fox"
        ll2._tail = LinkedList().Element(ll2,"The wary transgressor",None)
        #self.assertEqual(ll2.__dict__.get('_head').__dict__,ll2.__dict__.get('_tail').__dict__)
    
    def testExtract(self):
        try:
            ll = LinkedList()
            ll.append(1)
            ll.extract(1)
            self.assertIsNone(ll.getHead(),None)
            self.assertIsNone(ll.getTail(),None)
            ll.append(1)
            ll.append(2)
            ll.append(3)
            ll.append(4)
            ll.extract(2)
            self.assertIsNone(ll.getTail()._next,None)
        except AssertionError as error:
            self.assertEqual(error.message,'yoyo')
            
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()