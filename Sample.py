import torch
from FileDataset import FileDataset

from torch.utils.data import Dataset,DataLoader



if __name__ == "__main__":
    arr = FileDataset('./Data',100)
    arr.append(5)
    arr.append(6)
    arr.append(7)
    arr.append(8)
    arr.append(9)
    arr.append(10)
    print(arr)

    #to get batch of size 4
    loader = DataLoader(arr,batch_size=4,shuffle=True)
    nextval = iter(loader).next()
    print(nextval)
    nextval = iter(loader).next()
    print(nextval)