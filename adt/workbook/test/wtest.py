'''
Created on 5 Jun 2019

@author: anointedone
'''
import unittest
from adt.workbook.mymain import A

class Test(unittest.TestCase):


    def setUp(self):
        self._dynattr = A()
        


    def tearDown(self):
        pass


    def testDynattr(self):
        #self._dynattr.modify(A().Inner())
        
        tmp = A().Inner()
        tmp._attr = "Hello"
        self._dynattr._Aattr._attr = tmp
        #self._dynattr._Aattr = tmp
        self.assertIsNone(self._dynattr._Aattr)
        #self.assertEqual(self._dynattr._Aattr._attr,self._dynattr._Aattr._attr)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDynattr']
    unittest.main()