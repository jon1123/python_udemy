#######Lecture_8

import numpy as np

>>> 5/2
2
>>> 5.0/2
2.5
>>> from __furure__ import division
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named __furure__
>>> from __future__ import division
>>> arr1 = np.array([1,2,3,4],[8,9,10,11])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: data type not understood
>>> arr1 = np.array([[1,2,3,4],[8,9,10,11]])
>>> print arr1
[[ 1  2  3  4]
 [ 8  9 10 11]]
>>> arr1*arr1
array([[  1,   4,   9,  16],
       [ 64,  81, 100, 121]])
>>> arr1-arr1
array([[0, 0, 0, 0],
       [0, 0, 0, 0]])
>>> 1/arr1
array([[ 1.        ,  0.5       ,  0.33333333,  0.25      ],
       [ 0.125     ,  0.11111111,  0.1       ,  0.09090909]])
>>> arr1**3
array([[   1,    8,   27,   64],
       [ 512,  729, 1000, 1331]])

