import __init__
import settings.settings as settings
import helper.json_func as json_func
from logs.logger import logs_test, logs_sys, logs_dev, logging, lprint, has_exceed_multiple_logs

"""
Purpose: This files holds functions that will check if the files within the storage directory is stable
"""
class CheckFileStability:
    def run(file_path):
        if 'sample' in file_path:
            return CheckFileStability.sample_file(file_path)
        else:
            logs_sys.warning(f"CheckFileStability.run() ::: {file_path} is not a valid file path")
            return None
    
    def sample_file(file_path):
        """
        Description: This function will check if the sample_file.json file is stable. If not, it will restore it to its
            original state.
        """
        try:
            assert('sample' in file_path)
            logs_sys.info(f"sample_file() ::: {file_path} is stable")
            return True
        except Exception as e:
            logs_sys.warning(f"sample_file() ::: {file_path} is unstable")
        
        return False
    
if __name__ == '__main__':
    pass