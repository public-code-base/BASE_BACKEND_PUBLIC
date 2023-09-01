import __init__
import os
import shutil
import time
import storage.check_file_stability as check_file_stability
from logs.logger import logs_dev, logs_sys, logs_test, lprint

"""
Purpose: This files holds function that is used to backup files. This is then called by the "onchange" or "ontime" scheduler
"""

class BackupFiles:
    
    def run(monitored_file_path, backup_file_path, requirements_met=True):
        stability_result = check_file_stability.CheckFileStability.run(monitored_file_path)
        if stability_result == True:
            return BackupFiles.backup_file(monitored_file_path, backup_file_path, requirements_met)
        elif stability_result == False:
            return BackupFiles.restore_monitored_file(monitored_file_path, backup_file_path, requirements_met)
        elif stability_result == None:
            logs_sys.error(f"Error: Unable to check file stability for {monitored_file_path}")
            return 'failed'
    
    def backup_file(monitored_file_path, backup_file_path, requirements_met=True):
        """
        Description: The monitored_file_path is the file we are monitoring. This is for example:
                local_users.json. We have a backup file called local_users_backup.json.
            :param: monitored_file_path: str: "path/to/file.json"
            :param: backup_file_path: str: "path/to/file.json"
            :param: requirments_met: bool: True/False. This is a function we pass through so that we can check if the requirements
                has been met
        Purpose: The purpose of this function to backup the monitored file_path whenever there is a change.
        """
        if requirements_met:
            try:
                shutil.copyfile(monitored_file_path, backup_file_path)
                return 'success'
            except Exception as e:
                logs_sys.warning(f"Error: Unable to backup_file from {monitored_file_path} to {backup_file_path} ::: {e}")
        time.sleep(0.05)
        return 'failed'
    
    def restore_monitored_file(monitored_file_path, backup_file_path, requirements_met=True):
        """
        Description: The monitored_file_path is the file we are monitoring. This is for example:
                local_users.json. We have a backup file called local_users_backup.json.
            :param: monitored_file_path: str: "path/to/file.json"
            :param: backup_file_path: str: "path/to/file.json"
        Purpose: The purpose of this function is to restore the monitored file if it ends up getting corrupted by using the 
            backup file. The backup file is ensured to be only written to when its safe to write to the backup file.
        """
        if requirements_met:
            try:
                shutil.copyfile(backup_file_path, monitored_file_path)
                return 'success'
            except Exception as e:
                logs_sys.warning(f"Error: Unable to restore backup_file from {backup_file_path} to {monitored_file_path} ::: {e}")
        time.sleep(0.075)
        return 'failed'

    def save_global_states():
        """
        Description: The purpose of this function is save all of the GLOBAL settings to file. The reason being is that
            in the event of a disconnection/collapse, we have the states of the GLOBAL settings to be restored.
        """
        raise NotImplementedError
    
    def ensure_uncorrupted_files():
        """
        Description: The purpose of this function is to ensure that all the local files are not corrupted is updated to the latest
            is working at all times without getting corrupted. And if corrupted restore itself. First it does it by scanning all of
            the existing json files. Then for each file, save its content to firebase. In addition, save the uncorrupted state in a
            seperate self generating file. That directory houses all of the uncorrupted files. Each uncorrupted file is a copy of the
            original but also contains additional information of where the file is located. The backup uncorrupted file set will have
            the same leading names and will be ignored by gitignore.
        """
        raise NotImplementedError

if __name__ == '__main__':
    pass