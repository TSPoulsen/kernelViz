import os
import sys
sys.path.append(os.path.abspath( os.path.join(os.path.dirname(__file__), "../")))

print(sys.path)
from src.utils.data import ImagenetteDataset
from src.utils.constants import ROOT_PATH




imagenette_train = ImagenetteDataset(clean = True, original_meta = True)
imagenette_val = ImagenetteDataset(validation = True, clean = True, original_meta = True)

imagenette_train.saveMetaCSV(os.path.join(ROOT_PATH, "data", "imagenette2", "imagenette_train.csv"))
imagenette_val.saveMetaCSV(os.path.join(ROOT_PATH, "data", "imagenette2", "imagenette_val.csv"))







