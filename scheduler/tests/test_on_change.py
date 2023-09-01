import __init__
import pytest
import asyncio
import helper.json_func as json_func
import settings.settings as settings
import scheduler.on_change as on_change
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@pytest.mark.order(1)
@pytest.mark.parametrize("file_path, action, expected_result", 
        [('./scheduler/tests/test_on_change_add_watcher_sample0.json', None, 'success'),
         ('./scheduler/tests/test_on_change_add_watcher_sample0b.json', None, 'failed'),])
@decorator_testing
def test_OnChange_add_watcher(file_path, action, expected_result):
    # Arrange
    logs_sys.setLevel(logging.CRITICAL)
    # Act
    result = on_change.OnChange().add_watcher(file_path, action)
    # Assert
    assert(result == expected_result)
    # Reset
    logs_sys.setLevel(logging.DEBUG)
    
    
@pytest.mark.order(2)
@pytest.mark.parametrize("file_path, action, add_watcher, expected_result", 
        [('./scheduler/tests/test_on_change_add_watcher_sample0.json', None, True,'success'),
         ('./scheduler/tests/test_on_change_add_watcher_sample0.json', None, False,'failed'),])
@decorator_testing
def test_OnChange_remove_watcher(file_path, action, add_watcher, expected_result):
    # Arrange
    logs_sys.setLevel(logging.CRITICAL)
    if add_watcher: on_change.OnChange().add_watcher(file_path, action)
    # Act
    result = on_change.OnChange().remove_watcher(file_path)
    # Assert
    assert(result == expected_result)
    # Reset
    logs_sys.setLevel(logging.DEBUG)


@pytest.mark.order(3)
@pytest.mark.parametrize("file_path, action_type, args, expected_result", 
        [("./scheduler/tests/test_restore_monitored_file_sample1.json", "backup_file", {'backup_file_path': "./scheduler/tests/test_restore_monitored_file_sample2.json"},'success'),
         ("./scheduler/tests/test_restore_monitored_file_sample1.json", "backup_file", {'backup_file_path': None},'failed'),])
@decorator_testing
def test_OnChange_determine_action(file_path, action_type, args, expected_result):
    # Arrange
    logs_sys.setLevel(logging.CRITICAL)
    # Act
    result = on_change.OnChange().determine_action(file_path, action_type, args)
    # Assert
    assert(result == expected_result)
    # Reset
    logs_sys.setLevel(logging.DEBUG)


@pytest.mark.skip(reason="Skipping because only able to manually run")
@pytest.mark.order(4)
@pytest.mark.asyncio
@pytest.mark.parametrize("file_path, backup_file_path", 
        [('./scheduler/tests/test_on_change_monitor_changes_sample0.json', './scheduler/tests/test_on_change_monitor_changes_sample1.json')])
@decorator_testing
async def test_OnChange_monitor_changes(file_path, backup_file_path):
    # Arrange
    json_func.JsonFunc.update_json_file(file_path, "")
    json_func.JsonFunc.update_json_file(backup_file_path, "")
    on_change.OnChange().add_watcher(file_path, "backup_file", args={'backup_file_path': backup_file_path})
    # Act
    on_change_monitor_task = asyncio.create_task(on_change.OnChange().monitor_changes())
    # Assert
    await asyncio.sleep(1)
    json_func.JsonFunc.update_json_file(file_path, {'test': 'test'})
    await asyncio.sleep(2)
    settings.ASYNCIO_LOOP = False
    await on_change_monitor_task
    result = json_func.JsonFunc.get_json(file_path)
    backup_result = json_func.JsonFunc.get_json(backup_file_path)
    assert(result == backup_result)
    
if __name__ == '__main__':
    pass