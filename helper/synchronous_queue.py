import __init__
import queue
import asyncio
import settings.settings as settings
import threading
from logs.logger import logs_sys, lprint
from functools import wraps


"""
Purpose: The purpose of this file is to have a queue to pass background thread tasks to the main thread for execution.
    The reason for this is to avoid race conditions when using asyncio and threading.
"""

class SynchronousQueue:
    """
    Description: Pass functions from the background threads to the main thread for execution.
    Quick Links: https://medium.datadriveninvestor.com/the-most-simple-explanation-of-threads-and-queues-in-python-cbc206025dd1
    """
    def __init__(self):
        if (settings.FUNC_SYNC_INQUEUE == None or settings.FUNC_SYNC_OUTQUEUE == None):
            settings.FUNC_SYNC_INQUEUE = queue.Queue()
            settings.FUNC_SYNC_OUTQUEUE = queue.Queue()  # Define the output queue
            
    async def run(self):
        while settings.ASYNCIO_LOOP:
            await asyncio.sleep(0.01)
            if not settings.FUNC_SYNC_INQUEUE.empty():
                next_func = None
                next_func = settings.FUNC_SYNC_INQUEUE.get()
                if next_func != None:
                    result = next_func()
                    settings.FUNC_SYNC_OUTQUEUE.put(result)  # Put the result in the output queue
                settings.FUNC_SYNC_INQUEUE.task_done()
        
        logs_sys.info("FUNC_SYNC_INQUEUE.run() has stopped")

            


if __name__ == '__main__':
    pass