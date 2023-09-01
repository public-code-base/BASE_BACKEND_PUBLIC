import __init__
import os
import sys
import decimal
from logs.logger import logs_test, logs_sys, logging, logs_dev

def num_decimal_places(input):
    input = input + 1
    x = str(input)
    if "." in x:
        x = x.rstrip('0')
        x = decimal.Decimal(x)
        x = x.as_tuple().exponent
        x = abs(x)
        return x
    else:
        logs_sys.error("Failed: Attempting to find decimal places on non-float object")

def isfloat(num):
    try:
        if type(num) == float or type(num) == int or type(num) == str:
            float(num)
            return True
        else:
            raise ValueError
    except ValueError:
        return False
    
def isint(num):
    try:
        if type(num) == float or type(num) == int or type(num) == str:
            int(num)
            return True
        else:
            raise ValueError
    except ValueError:
        return False