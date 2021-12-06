# FileDataset

A pytorch dataset used for storing experience reply buffer in reinforcement learning on harddisk

Requirements :

- Pytorch
- pickle
- os
- glob

Files :

- FileDataset.py (implementation of pytorch dataset which stores on harddisk (not ram))
- Sample.py (a sample of how to add items and how to get shuffled batch)

Notes :

- if you have a ssd harddisk you will notice that no big difference between a ram list and a harddisk FileDataset in speed at starting training but you will find a big enhance with FileDataset in memory occupation and training speed after a 1000000 experience reply buffer becomes full
- if you restrart the application , the experience reply buffer will having the old buffer used last training which help in resuming training as Reinforcement learning may take serveral days training.

I hope you like this work
