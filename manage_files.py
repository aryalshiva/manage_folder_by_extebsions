import os
import shutil

def organize_files_by_extension(source_directory, destination_directory):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Loop through each file in the source directory
    for filename in os.listdir(source_directory):
        source_file = os.path.join(source_directory, filename)
        
        # Skip directories, only process files
        if os.path.isdir(source_file):
            continue
        
        # Get the file extension (e.g., .jpg, .pdf, etc.)
        file_extension = filename.split('.')[-1].lower()
        
        # Create a directory for the extension if it doesn't exist
        extension_folder = os.path.join(destination_directory, file_extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)
        
        # Move the file to the appropriate folder
        destination_file = os.path.join(extension_folder, filename)
        shutil.move(source_file, destination_file)
        print(f"Moved {filename} to {extension_folder}")

# Define source and destination directories
# PC_name should be replaced with your PC's name (e.g., Users/Shiva/Downloads)
# You can also change the destination directory to any folder you prefer
source_directory = r'C:\Users\PC_name\Downloads'  # Path to your Downloads folder
destination_directory = r'C:\Users\PC_name\Downloads\Organized'  # Organized folder inside Downloads

# Organize files
organize_files_by_extension(source_directory, destination_directory)

# To run this script, save it as manage_file.py and run it using Python
# Open a command prompt or terminal, navigate to the directory where the script is saved, and run:
# python manage_files.py run this command in the terminal or command prompt
