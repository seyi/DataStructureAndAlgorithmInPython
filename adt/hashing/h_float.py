'''
Created on 16 Jun 2019

@author: anointedone
'''
import math
class Float(float,object):
    
    def __hash__(self):
        (m,e) = math.frexp(self)
        mprime = int((abs(m) - 0.5) * (1L << 52))
        return mprime >> 20