import __init__
import asyncio
import settings.settings as settings
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

"""
Purpose: This files holds the main function to cancel, cancellable global loops
"""
class CancelLoop:
    def __init__(self):
        pass
    
    async def run(self):
        while settings.ASYNCIO_LOOP:
            await asyncio.sleep(1)
        for task in settings.GLOBAL_CANCELLABLE_LOOPS:
            task.cancel()
        logs_sys.info("CancelLoop.run() has stopped")
        
        
if __name__ == '__main__':
    pass