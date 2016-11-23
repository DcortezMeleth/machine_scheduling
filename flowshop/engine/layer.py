# coding=utf-8
from flowshop import LOOP_PRODUCT_TYPES_NO

__author__ = 'Bartosz Sądel'


class Layer(object):
    """Class representing layer in our simulation"""
    def __init__(self):
        self.machines = []
        self.tasks = {}
        for i in xrange(1, LOOP_PRODUCT_TYPES_NO):
            self.tasks[i] = 0
