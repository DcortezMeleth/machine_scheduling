# coding=utf-8
from flowshop.engine.model import Model

__author__ = 'Bartosz Sądel'


def main():
    model = Model()
    model._generate_order()
    print model._waitingOrders
    print model._nextOrderTurn
    for layer in model._layers:
        print layer, layer.next_step

if __name__ == '__main__':
    main()
