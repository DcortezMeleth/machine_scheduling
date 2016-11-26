# coding=utf-8
from flowshop.engine.model import Model

__author__ = 'Bartosz Sądel'


def main():
    model = Model()
    model._generate_order()
    print model.waitingOrders
    print model.layers[0].machines
    print model.layers[0].tasks
    print model.nextOrderTurn

if __name__ == '__main__':
    main()
