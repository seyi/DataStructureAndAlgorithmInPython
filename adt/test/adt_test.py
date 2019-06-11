'''
Created on May 28, 2019

@author: anointedone
'''
import unittest
from adt.abstractmethod import abstractmethod
from adt.Container import Container


class Test(unittest.TestCase):

    class MyCls(object):
        def sayHello(self):
            print('Hello')
        def greet(self):
            pass
        greet = abstractmethod(greet)

        def __get__(self,obj,type):
            print('GET CALLED')
        def __call__(self,*args,**kwargs):
            print('MYCLS BABY CALLED')

    class MyClsBaby(MyCls):
        def greet(self):
            print('Good morning sir')




    def setUp(self):
        #self._absm = abstractmethod()
        self._C = Container()
        self._Mc = self.MyCls()
        self._MyGreetInst = self.MyClsBaby()



    def tearDown(self):
        pass


    def testInit(self):
        # self._C.purge()
        pass

    def testGet(self):
        self._Mc.sayHello()

    def testGreeter(self):
        self._MyGreetInst.greet()
        self.MyCls.greet()




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()