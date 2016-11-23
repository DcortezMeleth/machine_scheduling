# coding=utf-8
import logging
import sys
import yaml

__author__ = 'Bartosz Sądel'

try:
    params = yaml.safe_load(open('../resources/config.yml'))
    PRODUCT_TYPES_NO = params['product_types']
    LOOP_PRODUCT_TYPES_NO = PRODUCT_TYPES_NO + 1

    logging.basicConfig(format=params['logging']['format'], filename=params['logging']['path'])

    print "Product types: " + str(PRODUCT_TYPES_NO)
except IOError as error:
    print 'Error while loading configuration file:\n' + str(error)
    sys.exit()
