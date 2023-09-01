#============================= REQUIRED FOR EACH .PY FILE =============================
ROOT_REPO = "BASE_BACKEND_PUBLIC"
import os, sys; 
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split(ROOT_REPO)[0]+ROOT_REPO)
ROOT_REPO = "src"
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split(ROOT_REPO)[0]+ROOT_REPO)
ROOT_REPO = "app"
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split(ROOT_REPO)[0]+ROOT_REPO)
import sys_paths
#============================= REQUIRED FOR EACH .PY FILE =============================