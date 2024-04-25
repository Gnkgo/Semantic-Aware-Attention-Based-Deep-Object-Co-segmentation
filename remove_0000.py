import os

# Path to the folder containing the images
folder_path = "Datasets/gnkgo/image"  # Change this to your folder path

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the filename ends with '0000' before the file extension
    if filename.endswith('0000.jpg') or filename.endswith('0000.png') or filename.endswith('0000.jpeg'):
        # New filename by removing the last 0000
        new_filename = filename[:-8] + filename[-4:]  # Removes the last 4 characters (0000) before the file extension
        # Get full path for old and new filenames
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed: {filename} to {new_filename}")
