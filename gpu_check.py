import torch

print("PyTorch Version:", torch.__version__)
print("Is CUDA Available:", torch.cuda.is_available())  
print("Device:", torch.device("cuda" if torch.cuda.is_available() else "cpu"))
