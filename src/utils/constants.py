import os
import re

PROJECT_NAME: str   = "kernelViz"
ROOT_PATH: str       = re.match(f".*\/{PROJECT_NAME}\/",os.path.abspath(__file__)).group()