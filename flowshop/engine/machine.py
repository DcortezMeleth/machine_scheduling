# coding=utf-8
import random
from flowshop import params

__author__ = 'Bartosz Sądel'


class Machine(object):
    """Class representing machine in our simulation"""

    def __init__(self, time_table):
        self.time_table = time_table
        self.product_type = 0
        self.turns_left = -1
        self.broken = False
        self.layer = None

    def set_layer(self, layer):
        """Sets reference to layer to which machines belong"""
        self.layer = layer

    def run(self):
        """Executes turn on machine"""
        if self._should_break():
            return
        self._decide_on_action()
        self._take_product()
        self.turns_left -= 1
        self._return_finished()

    def train(self):
        """Trains machine classifier"""
        pass  # TODO: add training

    def _decide_on_action(self):
        """Decides on next action"""
        if self.turns_left > 0:
            return
        pass  # TODO: add action choosing

    def _should_break(self):
        """Check if machine should break and if so performs necessary actions"""
        # if machine already broken decrease it's counter and return
        if self.broken:
            self.turns_left -= 1
            return True
        self.broken = True if random.randint(0, 100) < params['breaking_chance'] else False
        if self.broken:
            # if we are processing product we have to return it to the layer buffer
            if self.product_type > 0 and self.turns_left > 0:
                self.layer.tasks[self.product_type] += 1
            self.product_type = -1
            self.turns_left = params['break_time']
        return self.broken

    def _take_product(self):
        """Takes product from buffer if configured and buffer not empty"""
        if self.product_type <= 0 or self.layer.tasks[self.product_type] <= 0 or self.turns_left > 0:
            return
        self.layer.tasks[self.product_type] -= 1
        self.turns_left = self.time_table[self.product_type]

    def _return_finished(self):
        """If product is finished returns is to layer completed buffer"""
        if self.product_type > 0 >= self.turns_left:
            self.layer.completed_tasks[self.product_type] += 1
