# coding=utf-8
import numpy
from flowshop import LOOP_PRODUCT_TYPES_NO, params, PRODUCT_TYPES_NO
from flowshop.engine import subtract_products, add_products
from flowshop.engine.layer import Layer
from flowshop.engine.machine import Machine
from flowshop.engine.order import Order

__author__ = 'Bartosz Sądel'


class Model(object):
    """Class representing model in our simulation"""

    def __init__(self):
        self._nextOrderTurn = 0
        self._turnNo = 0
        self._layers = []
        self._waitingOrders = []
        self._finishedOrders = []
        self._completed = [0] * PRODUCT_TYPES_NO
        self._load_conf()
        self.history = []

    def run(self):
        """Runs experiment"""
        print '------------------------------------------------------'
        print '------------------ EXPERIMENT START ------------------'
        print '------------------------------------------------------'

        for i in xrange(1, params['turn_no']):
            print 'Start turn {}'.format(i)

            self._train()
            self._generate_order()
            for layer in self._layers:
                layer.run()
            self._deliver_orders()
            self._orders_tick()

        print '------------------------------------------------------'
        print '------------------ EXPERIMENT  STOP ------------------'
        print '------------------------------------------------------'

    def pass_products(self, products):
        """Adds products to completed products buffer"""
        add_products(self._completed, products)

    def get_state(self):
        """Returns model state"""
        state = []
        for layer in self._layers:
            state.extend(layer.tasks)
            state.extend(layer.get_machines_health())

    def _orders_tick(self):
        """Decreases waiting orders due time"""
        for order in self._waitingOrders:
            order.tick()

    def _train(self):
        """Trains classifiers in model"""
        for layer in self._layers:
            layer.train()

    def _deliver_orders(self):
        """Delivers orders which products are ready"""
        while True:
            order = self._waitingOrders[0]
            if subtract_products(self._completed, order.products):
                self._waitingOrders[:] = self._waitingOrders[1:]
                self._finishedOrders.append(order)
            else:
                break

    def _generate_order(self):
        """Generates order if appropriate turn"""
        if self._turnNo != self._nextOrderTurn:
            return
        order = Order()
        self._waitingOrders.append(order)
        self._layers[0].pass_products(order.products)
        self._nextOrderTurn += numpy.random.poisson() + 1

    def _load_conf(self):
        """Loads model configuration from yaml file"""
        for layer in reversed(params['layers']):
            machines = []
            for machine in layer['machines']:
                machines.append(Machine(machine['time_table']))
            self._layers.insert(0, Layer(machines, self, self._layers[0] if len(self._layers) else self))
