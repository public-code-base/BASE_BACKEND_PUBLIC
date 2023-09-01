import __init__
import os
import sys
import copy
import ast
import settings.settings as settings
import helper.file_manage as file_manage
from collections import Counter
from logs.logger import logs_test, logs_sys, logs_dev, lprint


class FileScan:
    
    def find_functions_in_python_file(self, file_path):
        methods = []
        o = open(file_path, "r")
        text = o.read()
        p = ast.parse(text)
        for node in ast.walk(p):
            if isinstance(node, ast.FunctionDef):
                methods.append(node.name)

        return methods
    
    def get_all_functions_in_project(self):
        all_py_files = self.get_all_python_files()
        functions_list = []
        for path in all_py_files:
            result = self.find_functions_in_python_file(path)
            functions_list.extend(result)
        return functions_list
    
    
    def get_all_python_files(self):
        """
        Purpose: Get all cleaned .py files
        """
        all_files = [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(settings.ROOT_DIR)] for val in sublist]
        cleaned_all_files = []
        for file in all_files:
            if file.endswith(".py"):
                if 'venv' not in file:
                    for ignored_file in settings.IGNORE_PY_FILES:
                        if ignored_file not in file:
                            cleaned_all_files.append(file)
                            
        return cleaned_all_files

    def get_all_test_python_files(self):
        cleaned_all_files = self.get_all_python_files()
        for file in copy.copy(cleaned_all_files):
            if 'test' not in file:
                cleaned_all_files.remove(file)
        return cleaned_all_files

    def get_all_test_functions_in_project(self):
        cleaned_all_files = self.get_all_test_python_files()
        functions_list = []
        for path in cleaned_all_files:
            result = self.find_functions_in_python_file(path)
            functions_list.extend(result)
            
        for i in copy.copy(functions_list):
            if not i.startswith("test_"):
                functions_list.remove(i)
                
        return functions_list
    
    def get_duplicates_in_functions_list(self):
        functions_list = self.get_all_test_functions_in_project()
        duplicates = []
        duplicates = [item for item, count in Counter(functions_list).items() if count > 1]
        return duplicates
    
    def check_duplicates_in_functions_list(self):
        duplicates_list = self.get_duplicates_in_functions_list()
        if len(duplicates_list) > 0:
            raise Exception("Duplicate test functions found: {}".format(duplicates_list))
        
        return duplicates_list
    
        
if __name__ == '__main__':
    pass