import __init__
import pytest
import settings.settings as settings
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@pytest.mark.order(1)
@pytest.mark.parametrize("", 
        [('')])
@decorator_testing
def test_CLASSNAME_FUNCTIONAME():
    # Arrange
    # Act
    # Assert
    # Cleanup
    pass

if __name__ == '__main__':
    pass