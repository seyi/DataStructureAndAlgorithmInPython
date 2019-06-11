'''
Created on May 27, 2019

@author: anointedone
'''
from time import time
if __name__ == '__main__':
    def compute_average(n):
        """Perform n appends to an empty list and return average time elapsed """
        data = []
        start = time()
        for k in range(n):
            data.append(None)
        end = time()
        return (end - start )/ n

    compute_average(64)