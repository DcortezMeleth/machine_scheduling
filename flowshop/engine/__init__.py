# coding=utf-8
from flowshop import PRODUCT_TYPES_NO

__author__ = 'Bartosz Sądel'


def subtract_products(target, source):
    """Subtracts values from dict source, from value if there is enough of them"""
    if not check_if_enough(target, source):
        return False
    for i in xrange(0, PRODUCT_TYPES_NO):
        target[i] -= source[i]
    return True


def add_products(target, source):
    """Subtracts values from dict source, from value if there is enough of them"""
    for i in xrange(0, PRODUCT_TYPES_NO):
        target[i] += source[i]


def check_if_enough(target, source):
    """Check whether target dict have at least as many products as source"""
    for i in xrange(0, PRODUCT_TYPES_NO):
        if target[i] < source[i]:
            return False
    return True
