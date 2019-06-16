'''
Created on 16 Jun 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.adt.hashing.h_float import Float


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testHash(self):
        f = Float(45.89)
        self.assertEqual(hash(f),8)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHash']
    unittest.main()