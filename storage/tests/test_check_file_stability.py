import __init__
import pytest
import settings.settings as settings
import storage.check_file_stability as check_file_stability
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint
    
    
    
@pytest.mark.order(4)
@pytest.mark.parametrize("file_path, expected_result", 
        [('./storage/tests/test_checkfilestability_all_tickers_list_sample0.json', True),
         ('./storage/tests/test_checkfilestability_all_tickers_list_sample1.json', True),
         ('./storage/tests/test_checkfilestability_all_tickers_list_false0.json', False)])
@decorator_testing
def test_CheckFileStability_sample_file(file_path, expected_result):
    # Arrange
    logs_sys.setLevel(logging.CRITICAL)
    # Act
    result = check_file_stability.CheckFileStability.sample_file(file_path)
    # Assert
    assert(result == expected_result)
    # Reset
    logs_sys.setLevel(logging.DEBUG)
    
    
@pytest.mark.order(5)
@pytest.mark.parametrize("file_path, expected_result", 
        [('./storage/tests/test_checkfilestability_all_tickers_list_sample1.json', True),
         ('./false_path', None)])
@decorator_testing
def test_CheckFileStability_run(file_path, expected_result):
    # Arrange
    logs_sys.setLevel(logging.CRITICAL)
    # Act
    result = check_file_stability.CheckFileStability.run(file_path)
    # Assert
    assert(result == expected_result)
    # Reset
    logs_sys.setLevel(logging.DEBUG)

if __name__ == '__main__':
    pass