import torch

# 0-D tensors (Scalar)
scalar = torch.tensor(7)
print("Scalar:", scalar)
print("Shape:", scalar.shape)

# 1-D tensors (Vector)
vector = torch.tensor([1.0, 2.0, 3.0])
print("Vector:", vector)
print("Shape:", vector.shape)

# 2-D tensors (Matrix)
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print("Matrix:", matrix)
print("Shape:", matrix.shape)

# 3-D tensors (stack of matrices)
tensor3d = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
print("3-D tensor:", tensor3d)
print("Shape:", tensor3d.shape)
