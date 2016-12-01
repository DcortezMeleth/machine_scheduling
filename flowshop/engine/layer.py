# coding=utf-8
from flowshop import PRODUCT_TYPES_NO
from flowshop.engine import add_products

__author__ = 'Bartosz Sądel'


class Layer(object):
    """Class representing layer in our simulation"""

    def __init__(self, machines, model, next_step):
        self._next_step = next_step
        self._machines = machines
        self.model = model
        for machine in self._machines:
            machine.set_layer(self)
        self.tasks = [] * PRODUCT_TYPES_NO
        self.completed_tasks = [] * PRODUCT_TYPES_NO

    def run(self):
        """Executes turn across layer"""
        for machine in self._machines:
            machine.run()
        self._next_step.pass_products(self.completed_tasks)

    def train(self):
        """Trains every machine"""
        for machine in self._machines:
            machine.train()

    def pass_products(self, products):
        """Adds products to layer buffer"""
        add_products(self.tasks, products)

    def get_machines_health(self):
        """Returns list of machines health"""
        health = []
        for machine in self._machines:
            health.append(machine.broken)

