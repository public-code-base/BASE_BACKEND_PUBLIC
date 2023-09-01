import __init__
import pytz
import logging
import datetime
import settings.settings as settings

class PSTFormatter(logging.Formatter):
    converter = lambda *args: datetime.datetime.now(pytz.timezone('US/Pacific')).timetuple()

"""
Purpose: This files holds all of the logging functions
Description: LOG FILES TO LOCAL DIRECTORY WITHIN LOGS FOLDER 
"""
class LogLocal:
    def __init__(self, file_name, overwrite="a"):
        self.initialize_log_alert(file_name)
        self.logger = logging.getLogger(file_name)
        if ((file_name != "logs_files_scans.log") or overwrite=="w"):
            self.logger.setLevel(logging.DEBUG)

            if (file_name == "logs_tests.log"):
                formatter = PSTFormatter("[%(asctime)s]:::%(levelname)s:::%(moduleA)s.%(funcNameA)s.%(kwargsA)s:::%(message)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")
            else:
                formatter = PSTFormatter("[%(asctime)s]:::%(levelname)s:::%(module)s.%(funcName)s:::%(message)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")
            # Here is where we set the time zone for the formatter
            # formatter.converter = lambda *args: pytz.timezone('US/Pacific').localize(datetime.datetime.utcnow()).astimezone().timetuple()

            if settings.ENVIRONMENT == "LOCAL":
                log_dir = settings.LOGGING_DIR + file_name
                file_handler = logging.FileHandler(log_dir, overwrite)
            else:
                file_handler = logging.StreamHandler()
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def initialize_log_alert(self, file_name):
        logging.ALERT = 49
        logging.addLevelName(logging.ALERT, "ALERT")
        def alert(self, message, *args, **kws):
            if self.isEnabledFor(logging.ALERT):
                # Yes, logger takes its '*args' as 'args'.
                self._log(logging.ALERT, message, args, **kws) 
        logging.Logger.alert = alert
    
    def get_logger(self):
        return self.logger

logs_sys = LogLocal("logs_system.log").get_logger()
logs_dev = LogLocal("logs_develop.log").get_logger()
logs_test = LogLocal("logs_tests.log").get_logger()

def lprint(*args, **kwargs):
    """
    Purpose: This function is used to print to the console and log files
    """
    print(*args, **kwargs)
    logs_dev.info(*args, **kwargs)


def has_exceed_multiple_logs(log_message, log_type="logs_sys",count=5, total_count=10):
    has_multiple_logs = False
    if log_type == "logs_sys": log_type_file = "logs_system.log"
    elif log_type == "logs_dev": log_type_file = "logs_develop.log"
    
    if log_type in settings.GLOBAL_PREVIOUS_LOG:
        if settings.GLOBAL_PREVIOUS_LOG[log_type]["previous_log"] == "":
            with open(f"./logs/{log_type_file}", 'r') as f:
                last_line = f.readlines()[-1]
                settings.GLOBAL_PREVIOUS_LOG[log_type]["previous_log"] = last_line.split("]")[1]
                settings.GLOBAL_PREVIOUS_LOG[log_type]["count"] = 0
                settings.GLOBAL_PREVIOUS_LOG[log_type]["total_count"] = 0
        
        if log_message in settings.GLOBAL_PREVIOUS_LOG[log_type]["previous_log"]:
            settings.GLOBAL_PREVIOUS_LOG[log_type]["count"] = settings.GLOBAL_PREVIOUS_LOG[log_type]["count"] + 1
            
        global_previous_log = settings.GLOBAL_PREVIOUS_LOG[log_type]["previous_log"]
        global_count = settings.GLOBAL_PREVIOUS_LOG[log_type]["count"]
        
        with open(f"./logs/{log_type_file}", 'r') as f:
            all_file = str(f.readlines())
            total_count_frequency = all_file.count(log_message)
            if total_count_frequency >= total_count:
                has_multiple_logs = True
                
        if global_count >= count:
            if log_message in global_previous_log:
                has_multiple_logs = True
    else:
        logs_sys.error(f"Invalid Log Type: {log_type}")
    
    return has_multiple_logs

if __name__ == "__main__":
    with open(f"./logs/logs_system.log", 'r') as f:
        last_line = str(f.readlines())
        result = last_line.count("INFO")
        print(result)