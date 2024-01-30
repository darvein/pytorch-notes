import torch
import numpy as np

# From Torch
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

# From Numpy
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

print(x_data)
print(x_np)
