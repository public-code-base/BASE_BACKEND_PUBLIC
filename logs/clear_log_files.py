import __init__
import os
import sys
import logging
import settings.settings as settings

"""
Purpose: This file is intended to provide a easy command line interface to clear log files
Description: 
    CLEAR LOCAL LOG FILES: If user types "python .\logs\clear_log_files.py 1", if "1" then
    delete the logs_develop.log file. If "2" prompt user if he is sure, deletes logs_system.log
"""

def clear_local_log_files(args_input):
    if args_input == "0":
        user_input = input('Are you sure you want to delete ALL LOG files? [Yes/No]\n')
        if user_input in ["y", "Y", "Yes", "yes"]: 
            if os.path.exists(settings.LOGGING_DIR):
                settings_LOGGING_DIR = os.listdir(settings.LOGGING_DIR)
                for item in settings_LOGGING_DIR:
                    if item.endswith(".log"):
                        try:
                            os.remove(os.path.join(settings.LOGGING_DIR, item))
                        except Exception as e:
                            print(f"Unable to remove: {os.path.join(settings.LOGGING_DIR, item)} - {e}")
            print('Removed all log files.\n')
        else: print('Aborted.\n')


    elif args_input == "1":
        file_name = "logs_develop.log"
        if os.path.exists(settings.LOGGING_DIR + file_name):
            os.remove(settings.LOGGING_DIR + file_name)
        print('Removed logs_develop.log file.\n')

    elif args_input == "2":
        file_name = "logs_system.log"
        user_input = input('Are you sure you want to delete "logs_system.log" file? [Yes/No]\n')
        if user_input in ["y", "Y", "Yes", "yes"]: 
            if os.path.exists(settings.LOGGING_DIR + file_name):
                os.remove(settings.LOGGING_DIR + file_name)
            print('Removed logs_system.log file.\n')

        else: print('Aborted.\n')
    
clear_local_log_files(sys.argv[len(sys.argv)-1])