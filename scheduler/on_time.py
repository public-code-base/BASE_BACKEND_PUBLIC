import __init__
import asyncio
import settings.settings as settings
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint


"""
Purpose: This files holds anything that is to be executed on a time based
"""
class OnTime:
    def __init__(self):
        pass
    
    async def add_watcher(self, time, func, *args, **kwargs):
        while settings.ASYNCIO_LOOP:
            func(*args, **kwargs)
            await asyncio.sleep(time)
        logs_sys.info(f"{func.__name__} has stopped")
    
    async def add_watcher_reversed(self, time, func, *args, **kwargs):
        while settings.ASYNCIO_LOOP:
            await asyncio.sleep(time)
            if asyncio.iscoroutinefunction(func):
                await func(*args, **kwargs)
            else:
                func(*args, **kwargs)
        logs_sys.info(f"{func.__name__} has stopped")
    
    

if __name__ == '__main__':
    pass