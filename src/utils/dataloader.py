from torch.utils.data import DataLoader


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


class DataLoader(DataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__(self, args, kwargs)






