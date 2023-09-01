import __init__
import pytest
import shutil
import settings.settings as settings
import scheduler.backup_files as backup_files
import helper.json_func as json_func
from helper.testing import decorator_testing
from logs.logger import logs_dev, logs_sys, logs_test, lprint

@pytest.mark.order(1)
@pytest.mark.parametrize("monitored_file_path, backup_file_path, requirements_met, expected_result1, expected_result2", 
        [("./scheduler/tests/test_backup_file_sample1.json","./scheduler/tests/test_backup_file_sample2.json",True, 'success', True),
         ("./scheduler/tests/test_backup_file_sample1.json","./scheduler/tests/test_backup_file_sample2.json",False, 'failed', False)])
@decorator_testing
def test_BackupFiles_backup_file(monitored_file_path, backup_file_path, requirements_met, expected_result1, expected_result2):
    # Arrange
    reset_path = './scheduler/tests/test_backup_file_sample0.json'
    shutil.copyfile(reset_path, backup_file_path)
    # Act
    result = backup_files.BackupFiles.backup_file(monitored_file_path, backup_file_path, requirements_met)
    # Assert
    assert(expected_result1 == result)
    monitored_file_path_value = json_func.JsonFunc.get_json(monitored_file_path)
    backup_file_path_value = json_func.JsonFunc.get_json(backup_file_path)
    compared_value = (monitored_file_path_value == backup_file_path_value)
    assert(compared_value == expected_result2)

@pytest.mark.order(2)
@pytest.mark.parametrize("monitored_file_path, backup_file_path, requirements_met, expected_result1, expected_result2", 
        [("./scheduler/tests/test_restore_monitored_file_sample1.json","./scheduler/tests/test_restore_monitored_file_sample2.json",True, 'success', True),
         ("./scheduler/tests/test_restore_monitored_file_sample1.json","./scheduler/tests/test_restore_monitored_file_sample2.json",False, 'failed', False)])
@decorator_testing
def test_BackupFiles_restore_monitored_file(monitored_file_path, backup_file_path, requirements_met, expected_result1, expected_result2):
    # Arrange
    reset_path = './scheduler/tests/test_restore_monitored_file_sample0.json'
    shutil.copyfile(reset_path, backup_file_path)
    # Act
    result = backup_files.BackupFiles.backup_file(monitored_file_path, backup_file_path, requirements_met)
    result = backup_files.BackupFiles.restore_monitored_file(backup_file_path, monitored_file_path, requirements_met)
    # Assert
    assert(expected_result1 == result)
    monitored_file_path_value = json_func.JsonFunc.get_json(monitored_file_path)
    backup_file_path_value = json_func.JsonFunc.get_json(backup_file_path)
    compared_value = (monitored_file_path_value == backup_file_path_value)
    assert(compared_value == expected_result2)
    
    
@pytest.mark.order(3)
@pytest.mark.parametrize("monitored_file_path, backup_file_path, requirements_met, expected_result1, expected_result2", 
        [("./scheduler/tests/test_restore_monitored_file_sample1.json","./scheduler/tests/test_restore_monitored_file_sample2.json",True, 'success', True),
         ("./scheduler/tests/test_restore_monitored_file_sample1.json","./scheduler/tests/test_restore_monitored_file_sample2.json",False, 'failed', False)])
@decorator_testing
def test_BackupFiles_run(monitored_file_path, backup_file_path, requirements_met, expected_result1, expected_result2):
    # Arrange
    reset_path = './scheduler/tests/test_restore_monitored_file_sample0.json'
    shutil.copyfile(reset_path, backup_file_path)
    # Act
    result = backup_files.BackupFiles.run(monitored_file_path, backup_file_path, requirements_met)
    # Assert
    assert(expected_result1 == result)
    monitored_file_path_value = json_func.JsonFunc.get_json(monitored_file_path)
    backup_file_path_value = json_func.JsonFunc.get_json(backup_file_path)
    compared_value = (monitored_file_path_value == backup_file_path_value)
    assert(compared_value == expected_result2)

if __name__ == '__main__':
    pass