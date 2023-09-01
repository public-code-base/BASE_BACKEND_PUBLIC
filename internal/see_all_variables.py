import __init__
import sys
import asyncio
import json
import settings.settings as settings
import helper.json_func as json_func
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint

"""
Purpose: This files sees all the variables of the program running. This is to diagnosis any memory
    issues such as continuously adding to a list. This is a very useful tool to see what is going on
"""
class SeeAllVariables:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    def get_by_module(self, module_name=None):
        if self.test_mode:
            module_name = sys.modules[__name__] if not module_name else module_name
            variables = [
                (key, value)
                for (key, value) in vars(module_name).items()
                if not key.startswith("_")
            ]
            
            logs_dev.info(f"======================================================")
            for (key, value) in variables:
                logs_dev.info(f"{key}: {sys.getsizeof(value)} Bytes")
                
            return "success"

    def write_to_json(self, file_location="./logs/logs_global_variables.json"):
        """
        Purpose: We need this function so that we can see all the global variable values.
            You will need to install the extension on your browser "JSONVue", go 
            into the settings and have it enabled to read files. Then open the file url
            in the browser. "file:///D:/YOUR_DIR/logs/logs_variables.json". This
            will allow you to see the global variables and their values while the program
            is running. It is used to diagonse to ensure that the flow of the program
            is working as intended.
        """
        if self.test_mode:
            module_name = settings
            module_name = sys.modules[__name__] if not module_name else module_name
            variables = [
                (key, value)
                for (key, value) in vars(module_name).items()
                if not key.startswith("_")
            ]
            variable_dict = {}
            excluded_list = ['FUNC_SYNC_QUEUE']
            included_list = ['LOGGING_DIR']
            
            for (key, value) in variables:
                if not key.islower():
                    if key not in excluded_list:
                        if key in included_list:
                            variable_dict[key] = value
                
            value = json_func.JsonFunc.update_json_file(file_location, variable_dict)
            return value
        

if __name__ == '__main__':
    result = SeeAllVariables(True).write_to_json()
    print(result)
