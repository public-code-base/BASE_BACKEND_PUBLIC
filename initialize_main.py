import __init__
import time
import asyncio
import queue
import gc
import settings.settings as settings
import helper.synchronous_queue as synchronous_queue
import helper.testing as testing
import internal.loop_verify as loop_verify
import internal.cancel_loop as cancel_loop
import api.api_endpoints as api_endpoints
from logs.logger import logs_sys, lprint
from logs.read_log_files import ReadLogFiles

"""
Purpose: This files runs anything we want to once.
Description: This file is especially useful if we want to ensure that it is ran on the main thread.
"""
async def initialize_main(intialize_list, test_mode=False):
    time.sleep(2)
    if test_mode: testing.enable_test_mode()
    gc.collect()
    tasks_list = []
    if intialize_list == 'all' or type(intialize_list) == list:
        num = 1
        if ((num in intialize_list) or (str(num) in intialize_list) or ('all' in intialize_list)):
            log_message = f"{str(num)}) Initialize the main thread sync queue."
            print(log_message)
            logs_sys.info(log_message)
            tasks_list.append(asyncio.create_task(synchronous_queue.SynchronousQueue().run()))
        num = num + 1
        if ((num in intialize_list) or (str(num) in intialize_list) or ('all' in intialize_list)):
            log_message = f"{str(num)}) Initializing the File Refresher for logs_system.log"
            print(log_message)
            logs_sys.info(log_message)
            tasks_list.append(asyncio.create_task(ReadLogFiles(settings.ROOT_DIR + settings.LOGGING_DIR + 'logs_system.log').continous_refresh()))
        num = num + 1
        if ((num in intialize_list) or (str(num) in intialize_list) or ('all' in intialize_list)):
            log_message = f"{str(num)}) Initializing Cancel Loop Listener"
            print(log_message)
            logs_sys.info(log_message)
            tasks_list.append(asyncio.create_task(cancel_loop.CancelLoop().run()))
        num = num + 1
        if ((num in intialize_list) or (str(num) in intialize_list) or ('all' in intialize_list)):
            log_message = f"{str(num)}) Loop Verify for Test Mode Only"
            print(log_message)
            logs_sys.info(log_message)
            tasks_list.append(asyncio.create_task(loop_verify.LoopVerify.run(5)))
        num = num + 1
        if ((num in intialize_list) or (str(num) in intialize_list) or ('all' in intialize_list)):
            log_message = f"{str(num)}) Initialize API Endpoints"
            print(log_message)
            logs_sys.info(log_message)
            api_endpoints.Server.start()
            
    else:
        logs_sys.error("Initialize_main: The initialize_list must be a list or 'all'.")

    try: 
        await asyncio.gather(*tasks_list)
    except Exception as e: 
        logs_sys.error(f"Program is about to crashloop error: {e}")

if __name__ == '__main__':
    asyncio.run(initialize_main(['all'], test_mode=True))