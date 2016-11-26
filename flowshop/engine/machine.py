# coding=utf-8
__author__ = 'Bartosz Sądel'


class Machine(object):
    """Class representing machine in our simulation"""
    def __init__(self, time_table):
        self.productType = -1
        self.timeTable = time_table
        self.turnsLeft = -1
        self.broken = False
