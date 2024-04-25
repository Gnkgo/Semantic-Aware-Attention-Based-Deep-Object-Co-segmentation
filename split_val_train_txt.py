import os
import random
from math import ceil

# Path to the folder containing the images
folder_path = "Datasets\gnkgo\label"  # Change this to your folder path

# List of all .png files in the folder
png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

#sort the list
png_files.sort()

# Determine the split index for training and validation
split_index = ceil(len(png_files) * 0.8)  # 4/5 for training, 1/5 for validation

# Split the list into training and validation sets
train_files = png_files[:split_index]
val_files = png_files[split_index:]


train_path = "Datasets\gnkgo\train.txt"
val_path = "Datasets\gnkgo\val.txt"

# Write the training filenames (without .png) to train.txt
with open('train.txt', 'w') as train_file:
    for filename in train_files:
        name_without_extension = filename[:-4]  # Remove the last 4 characters ('.png')
        train_file.write(f"{name_without_extension}\n")

# Write the validation filenames (without .png) to val.txt
with open('val.txt', 'w') as val_file:
    for filename in val_files:
        print("TEST")
        name_without_extension = filename[:-4]  # Remove the last 4 characters ('.png')
        val_file.write(f"{name_without_extension}\n")

print("Training and validation splits created successfully.")
