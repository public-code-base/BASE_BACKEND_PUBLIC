import __init__
import os
import settings.settings as settings
import scheduler.backup_files as backup_files
import storage.check_file_stability as check_file_stability
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint
"""
Purpose: This files holds the function that will ensure that all of the files are up to date. This
    is especially important ensuring that we have the correct tokens across main, tests, and backup files.
    This will also be ran once being embedded within the decorator testing.
"""
class StabilizeFiles:
    def __init__(self):
        pass
    
    def run(self, file_path_list):
        dict_file_paths = {}
        for file_path in file_path_list:
            dict_file_paths[file_path] = os.path.getmtime(file_path)
        dict_file_paths = dict(sorted(dict_file_paths.items(), key=lambda item: item[1],reverse=True))
        
        main_stable_file_path = None
        for file_path in dict_file_paths:
            result = check_file_stability.CheckFileStability.run(file_path)
            if result:
                main_stable_file_path = file_path
                break
        if main_stable_file_path != None:
            for file_path in dict_file_paths:
                if file_path != main_stable_file_path:
                    backup_files.BackupFiles.backup_file(main_stable_file_path, file_path)
        else:
            logs_sys.error("No stable file found. Please check the files.")


if __name__ == '__main__':
    pass