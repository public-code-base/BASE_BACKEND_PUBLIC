import __init__
import pytest
import settings.settings as settings
import helper.json_func as json_func
import internal.see_all_variables as see_all_variables
from helper.testing import decorator_testing
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

@decorator_testing
def test_SeeAllVariables_get_by_module():
    # Act
    result = see_all_variables.SeeAllVariables(test_mode=True).get_by_module(settings)
    # Assert
    assert(result == "success")


@decorator_testing
def test_SeeAllVariables_write_to_json():
    # Act
    result = see_all_variables.SeeAllVariables(test_mode=True).write_to_json()
    json_value = json_func.JsonFunc.get_json("./logs/logs_global_variables.json")
    # Assert
    assert(result == "success")
    assert(json_value["LOGGING_DIR"] == settings.LOGGING_DIR)
    
if __name__ == '__main__':
    pass