'''
Created on 16 Jun 2019

@author: anointedone
'''
import unittest

from datastructureandalgorithminpython.adt.hashing.h_string import String
class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testHash(self):
        s = String("ett")
        self.assertEqual(s.__hash__(),'ui')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHash']
    unittest.main()