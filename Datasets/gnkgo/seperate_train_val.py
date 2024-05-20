import shutil
import numpy as np
#train_names=np.genfromtxt("train.txt",dtype=str)
#print("train numbers",len(train_names))
#for train_name in train_names:
#    shutil.move('label/{}.png'.format(train_name), 'label/train/{}.png'.format(train_name))

val_names=np.genfromtxt("val.txt",dtype=str)
for val_name in val_names:
    extract_label = val_name[2]
    extract_label2 = val_name[3]
    print(extract_label)
    print(extract_label2)
    #shutil.move('train/{}.png'.format(val_name), 'val/{}.png'.format(val_name))
    shutil.move('train/{}.png'.format(extract_label), 'val/{}.png'.format(extract_label))
    shutil.move('train/{}.png'.format(extract_label2), 'val/{}.png'.format(extract_label2))