import torch.optim as optim
from torch.utils.data import DataLoader

from ImagesloaderRAM import *
from Burstload import *
from Trainfunction import *
from Savemodel import *
from Mycudatransformation import *
from MynnModule import *
from PSNR import *

import torchvision.transforms as T
import torchvision.utils as tu

import numpy as np

from time import time

dtype = torch.FloatTensor
gpu_dtype=torch.cuda.FloatTensor



"""
TO auto import modules
%load_ext autoreload
%autoreload 2

%reload_ext autoreload
"""



##

Denoiser, optimizer = Load_model('./25SFD_C_NB75000')

##

Denoiser=MFD_C(Denoiser).cuda()
loss = nn.L1Loss().cuda()




optimizer = optim.Adam(Denoiser.parameters(),lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.00001, amsgrad=False)


scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.9, patience=200, verbose=True, threshold=0.0001, threshold_mode='rel', cooldown=0, min_lr=0, eps=1e-08)



paths=['1','2','3']


##



trainburstserveur(Denoiser,paths, loss, optimizer, scheduler, Nb_frames =8, num_epochs = 5, nb_subepoch=200 ,save_every=1)






















