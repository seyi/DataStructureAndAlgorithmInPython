'''
Created on 16 Jun 2019

@author: anointedone
'''
import sys
class Integer(int , object):
    '''
    classdocs
    '''
    def __hash__(self):
        return self & sys.maxint
           
        