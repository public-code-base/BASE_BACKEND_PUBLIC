import __init__
import pytest
import asyncio
import settings.settings as settings
import internal.loop_verify as loop_verify
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@pytest.mark.order(1)
@pytest.mark.asyncio
@decorator_testing
async def test_LoopVerify__init__():
    # Arrange
    assert(settings.GLOBAL_STATE_MONITOR["CONTINUOUS_LOOP"]["LoopVerify"] == False)
    # Act
    created_task = asyncio.create_task(loop_verify.LoopVerify.run(0.5))
    await asyncio.sleep(0.2)
    settings.ASYNCIO_LOOP = False
    await asyncio.sleep(1)
    # # Assert
    assert(settings.GLOBAL_STATE_MONITOR["CONTINUOUS_LOOP"]["LoopVerify"] == True)
    

if __name__ == '__main__':
    pass