import __init__
import pytest
import random
import time
import helper.json_func as json_func
import settings.settings as settings
import storage.stabilize_files as stabilize_files
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@pytest.mark.order(1)
@pytest.mark.parametrize("file_path_list", 
        [(['./storage/tests/test_stabilize_files_sample0.json', 
           './storage/tests/test_stabilize_files_sample1.json', 
           './storage/tests/test_stabilize_files_sample2.json'])
         ])
@decorator_testing
def test_StabilizeFiles_run(file_path_list):
    # Arrange
    random_val = random.uniform(1.01, 100.01)
    file_change = random.choice([0, 1, 2])
    result = json_func.JsonFunc.update_json_file(file_path_list[file_change], random_val)
    # Act
    stabilize_files.StabilizeFiles().run(file_path_list)
    # Assert
    for file_path in file_path_list:
        value = json_func.JsonFunc.get_json(file_path)
        assert(value == random_val)


if __name__ == '__main__':
    pass