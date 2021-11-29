from torch.utils.data import Dataset
from torchvision.io import read_image
import torch
from .constants import ROOT_PATH
import pandas as pd

from typing import Tuple
import os
import logging



class ImagenetteDataset(Dataset):
    _imagenette_path: str = os.path.join(ROOT_PATH, "data", "imagenette2")
    _logger: logging.Logger = logging.getLogger("ImagenetteDataset")

    CODE_TO_NAME = dict(
        n01440764 = "tench",
        n02102040 = "English springer",   
        n02979186 = "cassette player", 
        n03000684 = "chain saw", 
        n03028079 = "church", 
        n03394916 = "French horn", 
        n03417042 = "garbage truck", 
        n03425413 = "gas pump", 
        n03445777 = "golf ball", 
        n03888257 = "parachute"
    )

    NAME_TO_CODE = {name: code for code, name in CODE_TO_NAME.items()}


    def __init__(self, validation: bool = False):
        self.metadata: pd.DataFrame = pd.read_csv( os.path.join(self._imagenette_path, "noisy_imagenette.csv") )
        self.metadata[self.metadata["is_valid"] == validation] # Filter out validation/train data
        self.metadata.rename(columns = {"noisy_labels_0" : "true_label"}, inplace = True)


    def __len__(self) -> int:
        return self.metadata.shape[0]
    
    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, str]:
        img_path: str = os.path.join(self._imagenette_path, self.metadata.iloc[idx]["path"])
        image: torch.Tensor = read_image(path = img_path)
        label: str = self.metadata.iloc[idx]["true_label"]
        return image, label










