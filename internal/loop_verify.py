import __init__
import asyncio
import settings.settings as settings
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

"""
Purpose: This files holds just a logging to logs_develop to see if the async function is not being stuck
    on any one function. This is only used for test_mode for initilize_main.py
"""
class LoopVerify:
    async def run(seconds=1):
        count = 0
        settings.GLOBAL_STATE_MONITOR["CONTINUOUS_LOOP"]["LoopVerify"] = True
        while settings.ASYNCIO_LOOP:
            logs_dev.info(f"LoopVerify: {count}")
            print(f"LoopVerify: {count}")
            count = count + 1
            await asyncio.sleep(seconds)
        logs_sys.info("LoopVerify.run() has stopped")

if __name__ == '__main__':
    pass