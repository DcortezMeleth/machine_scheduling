# coding=utf-8
from flowshop import LOOP_PRODUCT_TYPES_NO
from flowshop.engine import check_if_enough, subtract_products

__author__ = 'Bartosz Sądel'


class Model(object):
    """Class representing model in our simulation"""
    def __init__(self):
        self.layers = []
        self.waitingOrders = []
        self.finishedOrders = []
        self.completed = {}
        for i in xrange(1, LOOP_PRODUCT_TYPES_NO):
            self.completed[i] = 0

    def _deliver_orders(self):
        while True:
            order = self.waitingOrders[0]
            if subtract_products(self.completed, order.products):
                self.waitingOrders[:] = self.waitingOrders[1:]
                self.finishedOrders.append(order)
            else:
                break

    def _generate_order(self):
        pass

