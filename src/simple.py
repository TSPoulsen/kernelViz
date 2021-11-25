import torch
import logging
from utils import setupLogging 
from models import basicCNN

def run():
    setupLogging(use_time=True)
    logger: logging.Logger = logging.getLogger("simpleRunner")


if __name__ == "__main__":
    run()
