# encoding: utf-8
"""
@author: monitor1379 
@contact: yy4f5da2@hotmail.com
@site: www.monitor1379.com

@version: 1.0
@license: Apache Licence
@file: example1_3layers_nn.py
@time: 2016/10/9 17:45


"""

from hamaa.layers import Dense, Activation
from hamaa.models import Sequential
from hamaa.datasets import datasets
from hamaa.utils import np_utils
from hamaa.optimizers import SGD
import numpy as np
np.random.seed(0)

def run():

    model = Sequential()
    model.add(Dense(input_dim=2, output_dim=5, init='normal'))
    model.add(Activation('sigmoid'))
    model.add(Dense(output_dim=2))
    model.add(Activation('sigmoid'))
    model.set_loss('mse')
    model.set_optimizer(SGD(lr=0.9))

    print model.summary()

    x, y = datasets.load_moons_data(nb_data=400, noise=0.1)
    x -= x.mean(axis=0)
    x /= x.max(axis=0)
    y = np_utils.to_one_hot(y, 2)

    training_data, validation_data = np_utils.split_training_data(data=(x, y), split_ratio=0.9)

    model.train(training_data=training_data, nb_epochs=250, mini_batch_size=2, verbose=2,
                validation_data=validation_data, log_epoch=10)

    model.plot_prediction(data=training_data)
    model.plot_prediction(data=validation_data)
    model.plot_training_iteration()

if __name__ == '__main__':
    run()