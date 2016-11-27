# coding=utf-8
from flowshop import LOOP_PRODUCT_TYPES_NO
from flowshop.engine import add_products

__author__ = 'Bartosz Sądel'


class Layer(object):
    """Class representing layer in our simulation"""

    def __init__(self, machines, next_step):
        self.machines = machines
        self.tasks = {}
        self.next_step = next_step
        for i in xrange(1, LOOP_PRODUCT_TYPES_NO):
            self.tasks[i] = 0

    def run(self):
        """Executes turn across layer"""
        pass

    def pass_products(self, products):
        """Adds products to layer buffer"""
        add_products(self.tasks, products)
