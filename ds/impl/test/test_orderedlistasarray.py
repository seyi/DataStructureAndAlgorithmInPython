'''
Created on 12 Jun 2019

@author: anointedone
'''
import unittest
from datastructureandalgorithminpython.ds.impl.orderedlistasarray import OrderedListAsArray


class Test(unittest.TestCase):


    def setUp(self):
        self.ol  = OrderedListAsArray(5) 
        self.obj1 = [57]
        self.obj2 = [57]
        self.obj4 = ['A','B','C']
        self.obj5 = [59]
        self.ol.insert(self.obj1)
        
        self.ol.insert(self.obj2)
        self.ol.insert(self.obj4)
        self.ol.insert(self.obj5)
        self.obj3 = self.ol.find(self.obj1)
        self._cur = OrderedListAsArray.Cursor(self.ol,2)
        


    def tearDown(self):
        pass


    def testInsert(self):
        self.assertTrue(self.obj1 in self.ol)
        self.assertTrue(self.obj2 in self.ol)
        self.assertTrue(self.obj3 in self.ol)
        #print(OrderedListAsArray().insert.__doc__)
        
    def testWithdraw(self):
        self.assertEquals(self.ol.find(self.obj2),[57])
        self.ol.withdraw(self.ol.find(self.obj2))
        self.assertTrue(self.obj2 in self.ol)
        #print(OrderedListAsArray().withdraw.__doc__)
        
    def testCursor(self):
        self.assertEquals(self._cur.getDatum(),['A','B','C'])
        #print(OrderedListAsArray.Cursor.__doc__)
    def testFindPositiion(self):
        self.assertEqual(self.ol.findPosition(self.obj4)._offset,2)
        print(self.ol.findPosition.__doc__)
    def testgetitem(self):
        self.assertEqual(self.ol[3],[59])
        
    def testInsertAfter(self):
        self._cur.insertAfter([999])
        self.assertEqual(self.ol[4],[59])
        #print(self._cur.insertAfter.__doc__)
    def testInsertBefore(self):
        ol = OrderedListAsArray(4)
        ol.insert(1)
        ol.insert(3)
        ol.insert(4)
        c = OrderedListAsArray.Cursor(ol,1)
        c.insertBefore(2)
        c2 = OrderedListAsArray.Cursor(ol,3)
        
        #get the data just inserted
        d = c2.getDatum()
        self.assertEqual(d,4)
        #print(self._cur.insertBefore.__doc__)
        
        
    def testCursorWithdraw(self):
        ol = OrderedListAsArray(4)
        ol.insert(1)
        ol.insert(3)
        ol.insert(4)
        c = OrderedListAsArray.Cursor(ol,2)
        c.withdraw()
        c2 = OrderedListAsArray.Cursor(ol,0)
        c3 = OrderedListAsArray.Cursor(ol,2)
       
        #get the data just inserted
        d = c2.getDatum()
        self.assertEqual(d,1)
        print(self._cur.withdraw.__doc__)

        
    def testUsage(self):
        ol = OrderedListAsArray(4)
        ol.insert(1)
        ol.insert(2)
        c = OrderedListAsArray.Cursor(ol,0)
        c.insertAfter(3)
        c2 = OrderedListAsArray.Cursor(ol,1)
        #get the data just inserted
        d = c2.getDatum()
        self.assertEqual(d,3)
#3 is printed
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInsert']
    unittest.main()