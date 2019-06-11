'''
Created on 5 Jun 2019

@author: anointedone
'''

class A(object):
    def __init__(self):
            self._Aattr = self.Inner()
    def modify(self,v):            
            tmp = self.Inner()          
            tmp._attr = v
            self._Aattr._attr = tmp
            self._Aattr = tmp
    
    def getmyattr(self):
        return self._Aattr
   
    def setmyattr(self,value):
        self._Aattr = value
        
    myattr = property(
                fget = lambda self : self.getmyattr(),
                fset = lambda self, value : self.setmyattr(value))

                
    class Inner(object):
            def __init__(self):
                self._attr = None