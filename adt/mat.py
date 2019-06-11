'''
Created on 3 Jun 2019

@author: anointedone
'''

class Matrix(object):
    '''
    classdocs
    '''


    def __init__(self, numberofrows,numberofcolumns):
        '''
        Constructor
        '''
        assert(numberofrows >= 0)
        assert(numberofcolumns >= 0)
        super(Matrix, self).__init__()
        self._numberOfRows = numberofrows
        self._numberOfColumns = numberofcolumns
        
    def getNumberOfRows(self):
        return self._numberOfRows
    numberOfRows = property(
        fget = lambda self: self.getNumberOfRows())
    def getNumberOfColumns(self):
        return self._numberOfColumns
    numberOfColumns = property(
        fget = lambda self: self.getNumberOfColumns())
            
        