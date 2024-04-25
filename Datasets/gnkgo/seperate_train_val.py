import shutil
import numpy as np
train_names=np.genfromtxt("train.txt",dtype=str)
print("train numbers",len(train_names))
for train_name in train_names:
    shutil.move('label/{}.png'.format(train_name), 'label/train/{}.png'.format(train_name))

val_names=np.genfromtxt("val.txt",dtype=str)
for val_name in val_names:
    shutil.move('label/{}.png'.format(val_name), 'label/val/{}.png'.format(val_name))