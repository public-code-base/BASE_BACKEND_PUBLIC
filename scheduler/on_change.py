import __init__
import json
import os
import asyncio
import settings.settings as settings
import helper.json_func as json_func
import helper.file_manage as file_manage
import scheduler.backup_files as backup_files
from logs.logger import logs_dev, logs_sys, logs_test, lprint

class OnChange:
    def __init__(self):
        pass
        
    def add_watcher(self, file_path, action, args=None):
        """
        Description: This function will add a file watcher to the file path
        """
        if file_manage.check_file_exists(file_path):
            settings.GLOBAL_STATE_MONITOR["ON_CHANGE_FILE_WATCHER"][file_path] = {'action':action, 'args':args, 'last_change':os.path.getmtime(file_path)}
            watched = {file_path:action}
            logs_sys.info(f"OnChange.add_watcher() ::: Added {watched} to the file watcher")
            return "success"
        else:
            watched = {file_path:action}
            logs_sys.error(f"OnChange.add_watcher() ::: {watched} does not exist")
            return "failed"
    
    def remove_watcher(self, file_path):
        """
        Description: This function will remove a file watcher to the file path
        """
        if file_manage.check_file_exists(file_path):
            try:
                del settings.GLOBAL_STATE_MONITOR["ON_CHANGE_FILE_WATCHER"][file_path]
                logs_sys.info(f"OnChange.remove_watcher() ::: Removed {{file_path:action}} to the file watcher")
                return "success"
            except Exception as e:
                logs_sys.error(f"OnChange.remove_watcher() ::: {{file_path:action}} does not exist")
                return "failed"
        else:
            logs_sys.error(f"OnChange.remove_watcher() ::: {{file_path:action}} does not exist")
            return "failed"
    
    def determine_action(self, file_path, action_type, args):
        if action_type == "backup_file":
            if 'backup_file_path' in args:
                monitored_file_path = file_path
                backup_file_path = args['backup_file_path']
                return backup_files.BackupFiles.run(monitored_file_path, backup_file_path)
            else:
                logs_sys.error(f"OnChange.determine_action() ::: backup_file_path is not in args")
                
        elif action_type == "send_alert":
            raise NotImplementedError
        
        return 'failed'
    
    async def monitor_changes(self):
        """
        Description: If a change is detected in any of the files, update the last known change and run the action
        """
        while settings.ASYNCIO_LOOP:
            for file_path in settings.GLOBAL_STATE_MONITOR["ON_CHANGE_FILE_WATCHER"]:
                if file_manage.check_file_exists(file_path):
                    file_stat = os.path.getmtime(file_path)
                    if file_stat != settings.GLOBAL_STATE_MONITOR["ON_CHANGE_FILE_WATCHER"][file_path]['last_change']:
                        settings.GLOBAL_STATE_MONITOR["ON_CHANGE_FILE_WATCHER"][file_path]['last_change'] = file_stat
                        
                        action = settings.GLOBAL_STATE_MONITOR["ON_CHANGE_FILE_WATCHER"][file_path]['action']
                        args = settings.GLOBAL_STATE_MONITOR["ON_CHANGE_FILE_WATCHER"][file_path]['args']
                        self.determine_action(file_path, action, args)
                        
                else:
                    logs_sys.error(f"OnChange.monitor_changes() ::: {file_path} does not exist")
            await asyncio.sleep(0.5)
        logs_sys.info("OnChange.monitor_changes() has stopped")

if __name__ == '__main__':
    pass
        
    