'''
Created on 9 Jul 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.ds.impl.tree.generaltree import GeneralTree


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGetSubtree(self):
        d = GeneralTree("D")
        e = GeneralTree("E")
        d.attachSubtree(e)
        f = GeneralTree("F")
        e.attachSubtree(f)
        g = GeneralTree("G")
        h = GeneralTree("H")
        i = GeneralTree("I")
        g.attachSubtree(h)
        d.attachSubtree(g)
        h.attachSubtree(i)
        self.assertEqual(str(d),'hi')
        
        
        
        #self.assertEqual(str(d.getSubTree(2).getKey()),'G')
        #self.assertEqual(str(d.detachSubtree(e)),'E')
        self.assertEqual(str(d),'hi')
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetSubtree']
    unittest.main()