import sys
import os

'''
CONTROL All THE PACKAGE DIRECTORIES SO THAT IT POINTS TO EVERY FILE.
MAKE SURE EACH FILE NAME IS UNIQUE OTHERWISE YOU SYS_PATH WILL POINT TO THE FIRST SEEN FILE.
'''
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR_MOD_1 = ROOT_DIR + "/"
ROOT_DIR_MOD_2 = ROOT_DIR + "//"
ROOT_DIR_MOD_3 = ROOT_DIR + "\\"

SYS_PATHS = [
    ROOT_DIR,
    ROOT_DIR_MOD_1,
    ROOT_DIR_MOD_2,
    ROOT_DIR_MOD_3,
    "/home/runner/src/",
    "C:\\BASE_BACKEND_PUBLIC\\",
    "/app/"
]

sys.path.extend(SYS_PATHS)
sys.path = list(set(sys.path))