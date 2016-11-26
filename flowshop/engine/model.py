# coding=utf-8
import numpy
from flowshop import LOOP_PRODUCT_TYPES_NO, params
from flowshop.engine import subtract_products
from flowshop.engine.layer import Layer
from flowshop.engine.machine import Machine
from flowshop.engine.order import Order

__author__ = 'Bartosz Sądel'


class Model(object):
    """Class representing model in our simulation"""
    def __init__(self):
        self.nextOrderTurn = 0
        self.turnNo = 0
        self.layers = []
        self.waitingOrders = []
        self.finishedOrders = []
        self.completed = {}
        for i in xrange(1, LOOP_PRODUCT_TYPES_NO):
            self.completed[i] = 0
        self._load_conf()

    def run(self):
        print '------------------------------------------------------'
        print '------------------ EXPERIMENT START ------------------'
        print '------------------------------------------------------'

        for i in xrange(1, params['turn_no']):
            print 'Start turn {}'.format(i)

            self._train()
            self._generate_order()

        print '------------------------------------------------------'
        print '------------------ EXPERIMENT  STOP ------------------'
        print '------------------------------------------------------'

    def _train(self):
        pass

    def _deliver_orders(self):
        while True:
            order = self.waitingOrders[0]
            if subtract_products(self.completed, order.products):
                self.waitingOrders[:] = self.waitingOrders[1:]
                self.finishedOrders.append(order)
            else:
                break

    def _generate_order(self):
        if self.turnNo != self.nextOrderTurn:
            return
        order = Order()
        self.waitingOrders.append(order)
        self.layers[0].add_tasks(order.products)
        self.nextOrderTurn += numpy.random.poisson() + 1

    def _load_conf(self):
        for layer in reversed(params['layers']):
            machines = []
            for machine in layer['machines']:
                machines.append(Machine(machine['time_table']))
            self.layers.insert(0, Layer(machines, self.layers[0] if len(self.layers) else self))
