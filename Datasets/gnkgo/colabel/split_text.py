import random

# Path to the original dataset
original_file_path = 'Datasets/gnkgo/colabel/train_split.txt'

# Paths for training and validation files
train_file_path = 'Datasets/gnkgo/colabel/train.txt'
val_file_path = 'Datasets/gnkgo/colabel/val.txt'

# Read the original dataset
with open(original_file_path, 'r') as file:
    lines = file.readlines()
    print("TEST")


print(lines)
# Shuffle the dataset
random.shuffle(lines)

# Calculate the split index
split_index = int(0.8 * len(lines))  # 80% for training, 20% for validation

# Split into training and validation sets
training_lines = lines[:split_index]
validation_lines = lines[split_index:]

# Write the training set to a new file
with open(train_file_path, 'w') as train_file:
    train_file.writelines(training_lines)

# Write the validation set to a new file
with open(val_file_path, 'w') as val_file:
    val_file.writelines(validation_lines)

print("Dataset split into training and validation sets.")
