'''
Created on 3 Jun 2019

@author: anointedone
'''
from mat import Matrix
from adt.mda import MultiDimensionalArray
class DenseMatrix(Matrix):
    '''
    Dense Matrix
    '''


    def __init__(self, rows,columns):
        '''
        Constructor
        '''
        super(DenseMatrix, self).__init__(rows,columns)
        self._array = MultiDimensionalArray(rows,columns)
        
    def __getitem__(self,(i,j)):
        return self._array[i,j]
    def __setitem__(self,(i,j),value):
        self._array[i,j] = value
        