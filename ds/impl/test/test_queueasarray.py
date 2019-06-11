'''
Created on 10 Jun 2019

@author: anointedone
'''
import unittest
from ds.impl.queueasarray import QueueAsArray
from adt.exceptions.exceptions import ContainerEmpty


class Test(unittest.TestCase):


    def setUp(self):
        self._qarr = QueueAsArray(5)
        self._qarr.enqueue('The')
        self._qarr.enqueue('quick')
        self._qarr.enqueue('brown')
        self._qarr.enqueue('fox')


    def tearDown(self):
        pass


    def testEnqueue(self):
        self.assertEqual(self._qarr.getHead(), 'The')
        self.assertEqual(self._qarr.dequeue(),'The')
        self.assertEqual(self._qarr.dequeue(),'quick')
        self.assertEqual(self._qarr.dequeue(),'brown')
        self.assertEqual(self._qarr.dequeue(),'fox')
        self.assertRaises(ContainerEmpty,self._qarr.dequeue)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEnqueue']
    unittest.main()