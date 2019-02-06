#coding: utf-8

import os
import tensorflow as tf
import sys
sys.path.append("..")

from net.AlexNet import AlexNet, AlexNetConfig

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