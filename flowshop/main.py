# coding=utf-8
from flowshop.engine.order import Order

__author__ = 'Bartosz Sądel'


def main():
    orders = []
    for _ in xrange(1, 10):
        orders.append(Order())

if __name__ == '__main__':
    main()
