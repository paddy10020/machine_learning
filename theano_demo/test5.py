# coding:utf-8

import numpy as np
import theano
import theano.tensor as T
from numba.targets.numbers import bool_as_bool


def compute_accuracy(y_target, y_predict):
    correct_prediction = np.equal(y_predict, y_target)
    accuracy = np.sum(correct_prediction)/len(correct_prediction)
    return accuracy

rng = np.random

N = 400                     # training sample size
feats = 784                 # number of input variables

# generate a dataset: D = (input_values, target_class)
D = (rng.rand(N, feats), rng.randint(size=N, low=0, high=2))

# declare Theano symbolic variables
x = T.dmatrix('x')
y = T.dvector('y')

# initialize the weights and biases
W = theano.shared(rng.randn(feats), name='w')
b = theano.shared(0.1, name='b')

# construct theano expression graph
p_1 = T.nnet.sigmoid(T.dot(x, W) + b)
prediction = p_1 > 0.5
xent = -y * T.log(p_1) - (1 - y) * T.log(1 - p_1)
# 克服over feeding
cost = xent.mean() + 0.01 * (W**2).sum()
# cost = xent.mean()
gW, gb = T.grad(cost, [W, b])

# compile
learning_rate = 0.05
train = theano.function(inputs=[x, y],
                        outputs=[prediction, xent.mean()],
                        updates=((W, W-learning_rate*gW), (b, b-learning_rate*gb))
                        )
predict = theano.function(inputs=[x], outputs=prediction)

# training
for i in range(500):
    pred, err = train(D[0], D[1])
    if i % 50 == 0:
        print('cost', err)
        print('accuracy', compute_accuracy(D[1], predict(D[0])))

print('target values for D:')
print(D[1])
print('prediction on D:')
print(predict(D[0]))


