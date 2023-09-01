import __init__
import pytest
from helper.testing import decorator_testing
import settings.settings as settings
import internal.fix_pathing_slash as fix_pathing_slash
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@pytest.mark.order(1)
@pytest.mark.parametrize("root_path, file_path, expected_result", 
        [(settings.ROOT_DIR, settings.ROOT_DIR, settings.ROOT_DIR),
         ("d:/BASE_BACKEND_PUBLIC/", "path_1\\hello","path_1/hello"),
         ])
@decorator_testing
def test_helper_clean_path(root_path, file_path, expected_result):
    # Arrange
    settings.ROOT_DIR = root_path
    # Act
    result = fix_pathing_slash.helper_clean_path(file_path)
    # Assert
    assert(result == expected_result)
    # Reset
    settings.ROOT_DIR = "d:\\BASE_BACKEND_PUBLIC\\"

if __name__ == '__main__':
    pass