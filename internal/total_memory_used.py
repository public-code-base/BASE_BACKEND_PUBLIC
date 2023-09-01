import __init__
import psutil
import settings.settings as settings
from logs.logger import logs_sys, lprint

def get_memory_usage_mb():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_usage_mb = memory_info.rss / 1024 / 1024

    logs_sys.info(f"Total memory in use: {memory_usage_mb:.2f}MB")
    return memory_usage_mb