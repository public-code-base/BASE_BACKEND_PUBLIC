import __init__
import os
import settings.settings as settings
import internal.fix_pathing_slash as fix_pathing_slash
from logs.logger import logs_dev, logs_sys

"""
Purpose: This files holds the functions that will check the files in the directories and remove them
"""

def get_full_dir(directory):
    directory = directory.lstrip("./")
    directory = fix_pathing_slash.helper_clean_path(directory)
    directory = settings.ROOT_DIR + directory
    return directory

def check_file_exists(directory):
    file_exists = False
    error_message = None
    directory = get_full_dir(directory)
    
    if os.path.exists(directory):
        file_exists = True
    else:
        error_message = f"Attempting to check an non-existent directory/file: {directory}"
    
    if file_exists == True:
        error_message = None
        
    if error_message != None:
        logs_sys.error(error_message)
        
    return file_exists

def get_files_containing(directory, contains=None):
    files_containing = []
    if check_files_exists_containing(directory, contains):
        for item in os.listdir(directory):
            if item.__contains__(contains):
                files_containing.append(item)
                
    return files_containing

def check_files_exists_containing(directory, contains=None):
    file_exists = False
    error_message = None
    if os.path.exists(directory):
        if contains != None:
            for item in os.listdir(directory):
                if item.__contains__(contains):
                    file_exists = True
                else:
                    error_message = f"Directory does not have any file containing '{contains}'. Unable to check"
        else:
            file_exists = True
    else:
        error_message = f"Attempting to check an non-existent directory/file: {directory}"
    
    if file_exists == True:
        error_message = None
        
    if error_message != None:
        logs_sys.error(error_message)
        
    return file_exists

def remove_files_containing(directory, contains=None):
    removed = False
    error_message = None
    if os.path.exists(directory):
        if contains != None:
            for item in os.listdir(directory):
                if item.__contains__(contains):
                    if not directory.endswith("/"): directory = directory +"/"
                    os.remove(directory+item)
                    removed = True
                    logs_sys.info(f"Successfully removed the file: {directory+item}")
                else:
                    error_message = f"Directory does not have any file containing '{contains}'. Unable to remove"
        else:
            os.remove(directory)
            removed = True
            logs_sys.info(f"Successfully removed the file: {directory}")
    else:
        error_message = f"Attempting to remove an non-existent directory/file: {directory}"
        
    if removed == True:
        error_message = None
    
    if error_message != None:
        logs_sys.error(error_message)
        
    return error_message


if __name__ == '__main__':
    pass