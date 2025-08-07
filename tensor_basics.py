import torch

# Create a tensor
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print("x:\n", x)

# Create another tensor
y = torch.tensor([[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]])
print("y:\n", y)

# Element-wise Addition
z = x + y
print("x + y:\n", z)

# Matrix Multiplication
m = torch.matmul(x, y.T)
print("x * y.T (matrix multiply):\n", m)
