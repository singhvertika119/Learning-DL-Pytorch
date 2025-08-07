import torch

# Basic Arithmetic Operations
x = torch.tensor([2.0, 4.0, 6.0])
y = torch.tensor([1.0, 3.0, 5.0])

# Addition
print("Addition:", x + y)

# Subtraction
print("Subraction:", x - y)

# Multiplication
print("Multiplication:", x * y)

# Division
print("Division:", x / y)

# Matrix Multiplication
A = torch.tensor([[1, 2, 3], [4, 5, 6]])
B = torch.tensor([[1, 2], [3, 4], [5, 6]])

result = torch.matmul(A, B)
print("Matrix Multiplication:\n", result)

# Reshaping tensors
x = torch.arange(1, 7)
print("Original:", x)

reshaped = x.reshape(2, 3)
print("Reshaped:\n", reshaped)

# Squeezing and Unsqueezing
x = torch.tensor([[[1, 2, 3]]])

print("Squeezed:", x.squeeze())
print("Unsqeezed:", x.squeeze().unsqueeze(0))

# Transpose
x = torch.tensor([[1, 2], [3, 4]])
print("Original\n:", x)
print("Transpose\n:", x.T)

# Aggregation functions
x = torch.tensor([2.0, 4.0, 6.0])

print("Sum:", x.sum())
print("Mean:", x.mean())
print("Max:", x.max())
print("Index of max argument:", x.argmax())

# tensor indexing
x = torch.tensor([10, 20, 30, 40, 50])
print(x[0])
print(x[-1])

# tensor slicing
print(x[1:4])
print(x[:3])
print(x[::2])

# Mutidimensional indexing and slicing
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x[1, 2])
print(x[:, 1])
print(x[0])

# changing Data types
x = torch.tensor([1, 2,3])
x = x.type(torch.float32)
