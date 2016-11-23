# coding=utf-8
__author__ = 'Bartosz Sądel'


class Machine(object):
    """Class representing machine in our simulation"""
    def __init__(self):
        self.productType = -1
        self.timeTable = {}
        self.turnsLeft = -1
        self.broken = False
