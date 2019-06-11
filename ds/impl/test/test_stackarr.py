'''
Created on 7 Jun 2019

@author: anointedone
'''
import unittest
from ds.impl.StackArray import StackArray
from adt.exceptions.exceptions import ContainerEmpty


class Test(unittest.TestCase):


    def setUp(self):
        self._sa = StackArray(5)
        self._sa.push(1)
        self._sa.push('hello')
        self._sa.push('world')
        self._sa.push('of')
        self._sa.push('peace')


    def tearDown(self):
        pass


    def testInit(self):
        self.assertEqual(len(self._sa),5 )
        self.assertEqual(len(self._sa._array), 5)
        
    def testPush(self):
        sa = StackArray(4)
        sa.push(1)
        sa.push('hello')
        sa.push('world')
        self.assertEqual(3, len(sa))
        self.assertEqual(sa.getTop(), 'world')
        self.assertEqual(sa.pop(),"world")
        self.assertEqual(sa.pop(),"hello")
        self.assertEqual(sa.pop(),1)
        
    def testPurge(self):
        self._sa.purge()
        self.assertEqual(len(self._sa), 0)
        #self.assertEqual(self._sa.getTop(),"i")
        self.assertRaises(ContainerEmpty, self._sa.getTop)
        
    def testIter(self):
        sa =    StackArray(4)
        sa.push('hello')
        sa.push('world')
        sa.push('of')
        sa.push('peace')
        sa.__iter__().next()
        sa.__iter__().next()
        sa.__iter__().next()
        it = sa.__iter__()
        
        it.next()
        print('1 it var next: ' + it.__dict__.__str__())
        print('1 it var next: ' + it.__dict__.__str__())
        it.next()
        print('2 it var next: ' + it.__dict__.__str__())
        self.assertEquals(sa.__iter__().next(), 'hello')
        print('1 next: ' + sa.__iter__().__dict__.__str__())
        self.assertEquals(sa.__iter__().next(), 1)
        print('2 next: ' + sa.__iter__().__dict__.__str__())
        
        #it = self._sa.__iter__()
        #=======================================================================
        # self.assertEquals(it.next(), 1)
        # self.assertEquals(it.next(), 'hello')
        # self.assertEquals(it.next(), 'world')
        # self.assertEquals(it.next(), 'of')
        # self.assertEquals(it.next(), 'peace')
        # self.assertRaises(StopIteration,it.next)
        #     
        #=======================================================================
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()