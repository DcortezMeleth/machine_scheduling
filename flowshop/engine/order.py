# coding=utf-8
import random
from flowshop import PRODUCT_TYPES_NO
import flowshop

__author__ = 'Bartosz Sądel'

MIN_REWARD = flowshop.params['orders']['min_reward']
MAX_REWARD = flowshop.params['orders']['max_reward']
MIN_PENALTY = flowshop.params['orders']['min_penalty']
MAX_PENALTY = flowshop.params['orders']['max_penalty']
MIN_DUE_TIME = flowshop.params['orders']['min_due_time']
MAX_DUE_TIME = flowshop.params['orders']['max_due_time']


def generate_products():
    """Generates dict of products in one order based n configuration file"""
    products = [0] * PRODUCT_TYPES_NO
    if 'one_type' in flowshop.params['orders'] and flowshop.params['orders']['one_type']:
        if 'same_value' in flowshop.params['orders']:
            value = flowshop.params['orders']['same_value']
        else:
            value = random.randint(1, flowshop.params['orders']['max_value'])
        products[random.randint(0, PRODUCT_TYPES_NO - 1)] = value
    else:
        for i in xrange(0, PRODUCT_TYPES_NO):
            products[i] = random.randint(0, flowshop.params['orders']['max_value'])
    return products


class Order(object):
    """Order in simulation"""

    def __init__(self, reward=None, penalty=None, due_time=None, products=None):
        rand = random.Random()
        self.reward = reward if reward else rand.randint(MIN_REWARD, MAX_REWARD)
        self.penalty = penalty if penalty else rand.randint(MIN_PENALTY, MAX_PENALTY)
        self.due_time = due_time if due_time else rand.randint(MIN_DUE_TIME, MAX_DUE_TIME)
        self.products = products if products else generate_products()

    def __str__(self):
        return str(self.products)

    def tick(self):
        """Decreases due time of an order"""
        self.due_time -= 1
