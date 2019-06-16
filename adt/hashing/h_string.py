'''
Created on 16 Jun 2019

@author: anointedone
'''
import sys
class String(str,object):
    '''
    classdocs
    '''
    shift = 6
    mask = ~0 << (31 - shift)
    
    def __hash__(self):
        result = 0
        for c in self:
            result = ((result & String.mask) ^ result << String.shift \
                ^ ord(c)) & sys.maxint
                
        return result
    
    