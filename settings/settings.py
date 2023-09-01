import __init__
import time
import queue
import asyncio
import os
import internal.fix_pathing_slash as fix_pathing_slash
from decouple import config

ENVIRONMENT = config('ENVIRONMENT_TYPE')
FUNC_SYNC_INQUEUE = queue.Queue()
FUNC_SYNC_OUTQUEUE = queue.Queue()
ASYNCIO_LOOP = True
SERVER_THREAD = None
KNOWN_KTHREADS = []
GLOBAL_STATE_MONITOR = {
    'CONTINUOUS_LOOP':{
        'LoopVerify': False
    },
    'ON_CHANGE_FILE_WATCHER':{}
}

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).split("settings")[0]
LOGGING_DIR = "logs/"
LOCAL_STORAGE_DIR = "./storage/local_storage/"

GLOBAL_CANCELLABLE_LOOPS = []
"""
Description: GLOBAL_CANCELLABLE_LOOPS
Purporse: To prevent the log files from getting too big. We will deny the logs from being printed
    if the count exceeds 5. It will print the log that it has exceeded the number of reprints until the 
    log is different from what is currently trying to print out.
"""
GLOBAL_STATS = {
    "file_read_count": 0,
    "file_write_count": 0,
    "started_time": time.time(),
    "time_since_program_started": None
}
"""
Description: GLOBAL_STATS
Purporse: To collect stats of about the program. Example, the number of file reads and file writes.
"""
GLOBAL_PREVIOUS_LOG = {
    "logs_sys": {"previous_log": "", "count": 0, "total_count":0},
    "logs_dev": {"previous_log": "", "count": 0, "total_count":0}
}
"""
Description: GLOBAL_PREVIOUS_LOG
Purpose: To prevent the log files from getting too big. We will deny the logs from being printed
    if the count exceeds 5. It will print the log that it has exceeded the number of reprints until the 
    log is different from what is currently trying to print out.
"""

APP_NAME = config('APP_NAME')
VERSION = config('VERSION')
IGNORE_PY_FILES = [
    "__init__.py"
]
AES_KEY = config('AES_KEY')