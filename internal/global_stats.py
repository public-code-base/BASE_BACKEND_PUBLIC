import __init__
import time
import settings.settings as settings
import helper.get_time as get_time
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint
from functools import wraps

"""
Purpose: This files holds function for Global Stats
"""
class GlobalStats:
    def __init__(self):
        pass
    
    @staticmethod
    def decorator_file_read_count(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            settings.GLOBAL_STATS["file_read_count"] = settings.GLOBAL_STATS["file_read_count"] + 1
        wrapper.unwrapped = function
        return wrapper
        
    @staticmethod
    def decorator_file_write_count(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            settings.GLOBAL_STATS["file_write_count"] = settings.GLOBAL_STATS["file_write_count"] + 1
        wrapper.unwrapped = function
        return wrapper
    
    
    

if __name__ == '__main__':
    pass