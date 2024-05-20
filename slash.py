# Replace 'path_to_val_txt' with the actual path to your val.txt file
val_txt_path = "Datasets/gnkgo/colabel/train.txt"

# Read the contents of the file
with open(val_txt_path, 'r') as file:
    content = file.read()

# Replace all backslashes with forward slashes
updated_content = content.replace('\\', '/')

# Write the updated content back to the file
with open(val_txt_path, 'w') as file:
    file.write(updated_content)

print("All backslashes have been replaced with forward slashes in", val_txt_path)
