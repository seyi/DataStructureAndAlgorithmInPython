'''
Created on 9 Jun 2019

@author: anointedone
'''
import unittest
from ds.impl.stackaslinkedlist import StackAsLinkedList
from adt.exceptions.exceptions import ContainerEmpty
from ds.impl.m_visitor import MatchVisitor


class Test(unittest.TestCase):


    def setUp(self):
        self._sll2 = StackAsLinkedList()
        self._sll2.push('hello')
        self._sll2.push('world')
        self._sll2.push(None)
        self._sll2.push('peace')
        self._sll2.push('and')
        self._sll2.push('love')
        self._mv = MatchVisitor(None)
        
        


    def tearDown(self):
        pass


    def testPush(self):
        sll = StackAsLinkedList()
        sll.push('hello')
        sll.push('world')
        sll.push(None)
        sll.push('peace')
        sll.push('and')
        sll.push('love')
        self.assertEquals(sll.getTop(),'love')
        sll.pop()
        self.assertEquals(sll.getTop(),'and')
        self.assertEqual(sll.pop(),'and')
        self.assertEquals(sll.getTop(),'peace')
        sll.pop()
        sll.pop()
        sll.pop()
        sll.pop()
        self.assertRaises(ContainerEmpty, sll.pop)
        
    def testAccept(self):
        self._sll2.accept(self._mv)
        self.assertEqual(self._mv._found,'None as target')
    def testPop(self):
        self.assertEqual(self._sll2.pop(),'love')
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()