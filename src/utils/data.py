from torch.utils.data import Dataset
from torchvision.io import read_image
from torchvision.transforms import CenterCrop
import torch
from .constants import ROOT_PATH
import pandas as pd

from typing import Tuple, List  
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


    def __init__(self, image_size: Tuple[int,int] = (256,256), validation: bool = False, clean: bool = False):
        self.metadata: pd.DataFrame = pd.read_csv( os.path.join(self._imagenette_path, "noisy_imagenette.csv") )
        self.metadata = self.metadata[self.metadata["is_valid"] == validation] # Filter out validation/train data
        self.metadata.rename(columns = {"noisy_labels_0" : "true_label"}, inplace = True)

        self.image_size: Tuple[int,int] = image_size
        self.transformer = CenterCrop(image_size)

        if clean:
            self.__dropGreyscaled()


    def __len__(self) -> int:
        return self.metadata.shape[0]
    
    def __getitem__(self, idx: int, transform: bool = True) -> Tuple[torch.Tensor, str]:
        img_path: str = os.path.join(self._imagenette_path, self.metadata.iloc[idx]["path"])
        image: torch.Tensor = read_image(path = img_path)
        if transform:
            image = self.transformer(image)
        #self._logger.info(f"dim of {img_path} is: {image.shape}")
        label: str = self.metadata.iloc[idx]["true_label"]
        return image, label
    
    def __dropGreyscaled(self) -> None:
        i = 0
        mask = torch.ones(len(self.metadata))
        self._logger.debug("Removing all non RGB images")
        for i in range(len(self.metadata)):
            if i%1000 == 0: self._logger.debug(i)
            img, lab = self.__getitem__(i, transform = False)
            if img.shape[0] != 3:
                mask[i] = False
        # Drop all rows with indicies in the to_drop list
        self._logger.debug(f"In total removing {len(mask) - torch.sum(mask)}")
        self.metadata = self.metadata.loc[mask]
    
    def createMetaCSV() -> None:
        # TODO










