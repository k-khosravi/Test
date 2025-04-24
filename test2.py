import numpy as np


def sum_of_array(x):
    sum = 0
    for i in x:    
        sum += i
    return sum


x = np.array([1,2,3,4,5])

print(sum_of_array(x))