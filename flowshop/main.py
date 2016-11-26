# coding=utf-8
from flowshop.engine.model import Model

__author__ = 'Bartosz Sądel'


def main():
    model = Model()
    model._generate_order()
    print model.waitingOrders
    print model.nextOrderTurn
    for layer in model.layers:
        print layer, layer.next_step

if __name__ == '__main__':
    main()
