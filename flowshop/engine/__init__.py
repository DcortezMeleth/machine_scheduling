# coding=utf-8
__author__ = 'Bartosz Sądel'


def subtract_products(target, source):
    """Subtracts values from dict source, from value if there is enough of them"""
    if not check_if_enough(target, source):
        return False
    for key in target:
        target[key] -= source[key]
    return True


def add_products(target, source):
    """Subtracts values from dict source, from value if there is enough of them"""
    for key in target:
        target[key] += source[key]


def check_if_enough(target, source):
    """Check whether target dict have at least as many products as source"""
    for key in target:
        if target[key] < source[key]:
            return False
    return True
