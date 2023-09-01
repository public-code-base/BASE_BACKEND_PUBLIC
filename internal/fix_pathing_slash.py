import __init__
import settings.settings as settings

def helper_clean_path(file_path):
    """
    Purpose: Ensure that all the paths are in the correct format for multiple environments
    """
    if type(file_path) == str:
        if "./" in file_path:
            file_path = file_path.lstrip("./")
        if ".\\" in file_path:
            file_path = file_path.lstrip(".\\")
        if "/" in settings.ROOT_DIR:
            file_path = file_path.replace("\\", "/")
        if "\\" in settings.ROOT_DIR:
            file_path = file_path.replace("/", "\\")
        if "\n" in settings.ROOT_DIR:
            file_path = file_path.replace("\n", "")

    return file_path