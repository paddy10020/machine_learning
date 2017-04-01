# coding:utf-8
# theano的一些简单使用

import numpy as np
import theano.tensor as T
from theano import function
from theano import pp
# basic
a = T.dscalar('a')
b = T.dscalar('b')
c = a*b
f = function([a, b], c)
d = f(1.5, 3)
print(d)

# to pretty-print the function
print(pp(c))

# how about matrix
x = T.dmatrix('x')
y = T.dmatrix('y')
# simple multiplication
z = x * y
# matrix multiplication
# z = T.dot(x, y)
f = function([x, y], z)
print(f(np.arange(12).reshape((3, 4)), 10*np.ones((3, 4))))

