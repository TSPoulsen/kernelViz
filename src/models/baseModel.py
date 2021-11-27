import torch
from torch import nn
from typing import Tuple, Optional


class BaseModel(nn.Module):
    def __init__(self, ):
        super().__init__()
        # _input_dims are of (height, width, depth/colors)
        _input_dims: Tuple[int,int,int] = None

        pass

    def getInputShape(self) -> Optional[Tuple[int,int,int]]:
        """
        Returns the needed shape of an individual sample as (height, width, colors)
        """
        return self._input_shape

    def __call__(self, x : torch.Tensor) -> torch.Tensor:
        """
        Gives prediction for each input in Tensor
        Input is expected to be of shape (x_samples, height, width, colors)
        The shape of each individual sample is given by self._input_shape which should be specified by specialization class
        It can be retrieved by calling the method getInputDims()
        
        """
        assert self._input_shape != None, "_input_dims must be specified by specialization class, to ensure input is of correct dimensionality"
        assert self._output_dims != None, "_output_dims must be specified by specialization class, to ensure output is of correct dimensionality"

        input_sample_shape = tuple(x.shape[1:])
        if len(x.shape) == 3:
            input_sample_shape = tuple(x.shape)
            # only a single sample is given as input
        assert input_sample_shape == self._input_shape, "Sample does not conform to specified dimensionality.\n \
                                                        Each input image is expected to be of shape {self._input_shape}, but was actually of shape {input_sample_shape}" 

        # Check input dimensionality to fit what is specified
        output = self.forward(x) # Must be implemented by specialization class
        expected_output_shape = tuple(x.shape[0])
        if len(x.shape) == 3:
            expected_output_shape = (1)

        assert output.shape == expected_output_shape, f"Error made in forward method, as output does not match expected output shape\n \
        expected output to be of shape {expected_output_shape} but it was actually of shape {output.shape}"
