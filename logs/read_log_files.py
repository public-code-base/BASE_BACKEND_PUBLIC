import __init__
import os
import asyncio
import datetime
import settings.settings as settings
from internal.fix_pathing_slash import helper_clean_path
from logs.logger import logs_dev, logs_sys

class ReadLogFiles:
    def __init__(self, file_path):
        self.file_path = helper_clean_path(file_path)
        self.log_file = None
        if os.path.exists(file_path):
            self.log_file = open(file_path, 'r')
    
    def get_log_file(self):
        return self.log_file
    
    def get_log_file_read(self):
        return self.log_file.read()
    
    def does_error_exist(self):
        if self.log_file != None:
            if "ERROR" in self.log_file.read():
                return True
        return False
    
    def get_warning_line(self):
        if self.log_file != None:
            for line in reversed(self.log_file.readlines()):
                if "WARNING" in line:
                    return line
        return None
    
    def get_error_line(self):
        if self.log_file != None:
            for line in reversed(self.log_file.readlines()):
                if "ERROR" in line:
                    return line
        return None
    
    def get_alert_line(self):
        if self.log_file != None:
            for line in reversed(self.log_file.readlines()):
                if "ALERT" in line:
                    return line
        return None
    
    def get_error_or_alert_line(self):
        if self.log_file != None:
            for line in reversed(self.log_file.readlines()):
                if "ALERT" in line:
                    return line
                if "ERROR" in line:
                    return line
        return None
    
    def get_timestamp(self, line_str=None):
        line_str = line_str.rsplit("]")[0].strip("[")
        return datetime.datetime.strptime(line_str,'%m/%d/%Y %I:%M:%S %p %Z').timestamp()
    
    def get_parsed_block_log_time_and_line(self, line_str):
        block_str = ""
        if type(line_str) == str:
            list_line_str = line_str.split(":::")
            for each_ele in list_line_str:
                block_str = block_str + each_ele + "\n"
            
        return block_str
    
    async def continous_refresh(self):
        while settings.ASYNCIO_LOOP:
            open(self.file_path, 'r').close()
            await asyncio.sleep(0.1)
        logs_sys.info("ReadFileLogs.continous_refresh() has stopped")
    
    def simple_refresh(self):
        open(self.file_path, 'r').close()