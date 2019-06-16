'''
Created on 16 Jun 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.adt.association import Association


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testHash(self):
        assoc =  Association('name','seyi')
        self.assertEquals(hash(assoc),0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHash']
    unittest.main()