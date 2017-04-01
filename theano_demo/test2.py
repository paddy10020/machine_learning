# coding:utf-8

import numpy as np
import theano.tensor as T
import theano
from theano import function

# activation function example
x = T.dmatrix('x')
s = 1/(1 + T.exp(-x))  # logistic or soft step
logistic = function([x], s)
print(logistic([[0, 1], [2, 3]]))

# multiply outputs for a function
a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
squared_diff = diff**2
f = function([a, b], [diff, abs_diff, squared_diff])
print(f(np.ones((2, 2)), np.arange(4).reshape((2, 2))))

# name for a function
x, y, w = T.dscalars('x', 'y', 'w')
z = (x + y) * w
# 设定默认值
f = function([x, theano.In(y, value=1), theano.In(w, value=2, name='weights')], z)
print(f(23, ))
print(f(23, weights=4))
