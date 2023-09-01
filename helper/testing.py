import __init__
import asyncio
import pytest
import exception_errors.exception_errors as exception_errors
import settings.settings as settings
import storage.stabilize_files as stabilize_files
from functools import wraps
from logs.logger import logs_test

"""
Purpose: This files holds all of the decorators for testing
"""
def enable_test_mode():
    pass

def async_testing(coroutine):
    """
    Purpose: A decorator for async function testing
    """
    @wraps(coroutine)
    async def wrapper(tf_print=True, *args, **kwargs):
        try:
            value = await coroutine(*args, **kwargs)
            logs_test.info(f"Test Passed", extra={'moduleA': coroutine.__module__, 'funcNameA': coroutine.__name__, 'kwargsA': str(kwargs)})
            if tf_print == True: print("Passed")
        except Exception as e:
            logs_test.error(f"Test Failed: {e}", extra={'moduleA': coroutine.__module__, 'funcNameA': coroutine.__name__, 'kwargsA': str(kwargs)})
            if tf_print == True: print(f"Failed: {e}")
            raise exception_errors.TestFailed(f"Test Failed: {e}")
        return value
    return wrapper

def sync_testing(function):
    """
    Purpose: A decorator for synchronous function testing
    """
    @wraps(function)
    def wrapper(tf_print=True, *args, **kwargs):
        try:
            function(*args, **kwargs)
            logs_test.info(f"Test Passed", extra={'moduleA': function.__module__, 'funcNameA': function.__name__, 'kwargsA': str(kwargs)})
            if tf_print == True: print("Passed")
        except Exception as e:
            logs_test.error(f"Test Failed: {e}", extra={'moduleA': function.__module__, 'funcNameA': function.__name__, 'kwargsA': str(kwargs)})
            if tf_print == True: print(f"Failed: {e}")
            raise exception_errors.TestFailed(f"Test Failed: {e}")
    wrapper.unwrapped = function
    return wrapper

def decorator_testing(function_or_coroutine):
    """
    Purpose: A decorator for testing both synchronous and asynchronous functions
    """
    enable_test_mode()
    if asyncio.iscoroutinefunction(function_or_coroutine):
        return async_testing(function_or_coroutine)
    else:
        return sync_testing(function_or_coroutine)

if __name__ == '__main__':
    pass