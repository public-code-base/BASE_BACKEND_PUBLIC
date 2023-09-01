import __init__
import pytest
import settings.settings as settings
import internal.global_stats as global_stats
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@pytest.mark.order(1)
@decorator_testing
def test_GlobalStats_decorator_file_read_count():
    # Arrange
    settings.GLOBAL_STATS["file_read_count"] = 0
    @global_stats.GlobalStats.decorator_file_read_count
    def sample_run():
        pass
    # Act
    sample_run()
    # Assert
    assert(settings.GLOBAL_STATS["file_read_count"] == 1)

@pytest.mark.order(2)
@decorator_testing
def test_GlobalStats_decorator_file_write_count():
    # Arrange
    settings.GLOBAL_STATS["file_write_count"] = 0
    @global_stats.GlobalStats.decorator_file_write_count
    def sample_run():
        pass
    # Act
    sample_run()
    # Assert
    assert(settings.GLOBAL_STATS["file_write_count"] == 1)

if __name__ == '__main__':
    pass