# coding=utf-8
import numpy
from flowshop import LOOP_PRODUCT_TYPES_NO, params
from flowshop.engine import subtract_products, add_products
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
        """Runs experiment"""
        print '------------------------------------------------------'
        print '------------------ EXPERIMENT START ------------------'
        print '------------------------------------------------------'

        for i in xrange(1, params['turn_no']):
            print 'Start turn {}'.format(i)

            self._train()
            self._generate_order()
            for layer in self.layers:
                layer.run()
            self._deliver_orders()
            self._orders_tick()

        print '------------------------------------------------------'
        print '------------------ EXPERIMENT  STOP ------------------'
        print '------------------------------------------------------'

    def pass_products(self, products):
        """Adds products to completed products buffer"""
        add_products(self.completed, products)

    def _orders_tick(self):
        """Decreases waiting orders due time"""
        for order in self.waitingOrders:
            order.tick()

    def _train(self):
        """Trains classifiers in model"""
        for layer in self.layers:
            layer.train()

    def _deliver_orders(self):
        """Delivers orders which products are ready"""
        while True:
            order = self.waitingOrders[0]
            if subtract_products(self.completed, order.products):
                self.waitingOrders[:] = self.waitingOrders[1:]
                self.finishedOrders.append(order)
            else:
                break

    def _generate_order(self):
        """Generates order if appropriate turn"""
        if self.turnNo != self.nextOrderTurn:
            return
        order = Order()
        self.waitingOrders.append(order)
        self.layers[0].pass_products(order.products)
        self.nextOrderTurn += numpy.random.poisson() + 1

    def _load_conf(self):
        """Loads model configuration from yaml file"""
        for layer in reversed(params['layers']):
            machines = []
            for machine in layer['machines']:
                machines.append(Machine(machine['time_table']))
            self.layers.insert(0, Layer(machines, self.layers[0] if len(self.layers) else self))
