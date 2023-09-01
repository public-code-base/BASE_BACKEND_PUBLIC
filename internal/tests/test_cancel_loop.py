import __init__
import pytest
import asyncio
import settings.settings as settings
import internal.cancel_loop as cancel_loop
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@pytest.mark.order(1)
@pytest.mark.asyncio
@decorator_testing
async def test_CancelLoop_run():
    # Arrange
    async def test_loop():
        while True:
            await asyncio.sleep(10)
    loop = asyncio.get_event_loop()
    settings.GLOBAL_CANCELLABLE_LOOPS.append(loop.create_task(test_loop()))
    # Act
    created_task = asyncio.create_task(cancel_loop.CancelLoop().run())
    # Assert
    settings.ASYNCIO_LOOP = False
    await asyncio.sleep(1.1)
    for task in settings.GLOBAL_CANCELLABLE_LOOPS:
        assert(task.cancelled() == True)

if __name__ == '__main__':
    pass