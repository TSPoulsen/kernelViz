import torch
import logging
from utils import setupLogging 
from utils.data import ImagenetteDataset
from torch.utils.data import DataLoader, Dataset
from models import simpleCNN

def run():
    setupLogging(use_time=True)
    logger: logging.Logger = logging.getLogger("simpleRunner")

    imagenette_train: Dataset = ImagenetteDataset()
    #imagenette_val:   Dataset = ImagenetteDataset(validation = True)
    train_loader: DataLoader = DataLoader(imagenette_train, batch_size = 64, shuffle=True)
    #val_loader:   DataLoader = DataLoader(imagenette_val)

    for batch in iter(train_loader):
        print(batch)
        break









if __name__ == "__main__":
    run()
