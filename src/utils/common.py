import os
import sys
import re
import logging
from typing import Optional

from .constants import * 

def setupLogging(log_file_path: Optional[str] = None, use_time: bool = False) -> None:
    """
    Runs the setup for the logging module.
    To retrieve a logger call logging.getLogger(<name>)
    default log_file_path is ROOT_PATH/log.txt
    """
    time_format = "%m-%d %X"

    output_format: str = "%(asctime)s " if use_time else "" 
    output_format += "%(levelname)s\t%(name)12s: %(message)s"

    if log_file_path == None: 
        log_file_path = os.path.join(ROOT_PATH,"log.txt")
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    stdout_handler: logging.StreamHandler = logging.StreamHandler(stream = sys.stdout)

    file_handler:   logging.FileHandler   = logging.FileHandler(filename = log_file_path)
    stdout_handler.setLevel(logging.WARNING)

    logging.basicConfig(datefmt=time_format,
                        format=output_format,
                        handlers=[file_handler, stdout_handler],
                        level = logging.DEBUG
                        )
    return



