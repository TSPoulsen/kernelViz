import torch 
import torch.nn as nn
from .baseModel import BaseModel

class simpleCNN(BaseModel):

    def __init__(self):
        super().__init__()