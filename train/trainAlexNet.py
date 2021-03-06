#coding: utf-8

"""
Fangrui Liu     mpskex@github   mpskex@163.com
Department of Computer Science and Technology
Faculty of Information
Beijing University of Technology
Copyright 2019
"""

import os
import tensorflow as tf
import sys
sys.path.append("..")

from classifiers.AlexNet import AlexNet, AlexNetConfig

if __name__ == '__main__':
    config = AlexNetConfig()
    config.read('../config/AlexNet.cfg')
    config.bound(train_flag=True)
    config.print_config()

    from tensorflow.examples.tutorials.mnist import input_data
    mnist = input_data.read_data_sets(config.mnist_data, reshape=False, one_hot=True)
    

    model = AlexNet(config=config,
                    dataset = mnist,
                    training=True,
                    )
    model.BuildModel()
    model.train()