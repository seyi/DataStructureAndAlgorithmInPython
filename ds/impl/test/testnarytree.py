'''
Created on 18 Jul 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.ds.impl.tree.narytree import NaryTree


class Test(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInit(self):
        n3tree = NaryTree(3,"A")
        self.assertEqual(str(n3tree), '{A}')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()