import os
import sys
import shutil
from datetime import datetime

# This function does the backup
def backup_files(source, destination):

    # Check for Source directory
    if not os.path.exists(source):
        print(f"Error : Source directory '{ source }' does not exist.")
        return
    
    # Check for Destination directory
    if not os.path.exists(destination):
        print(f"Error: Destination directory '{destination}' does not exist.")
        return
    
    # Go through all the files in the source folder
    for file_name in os.listdir(source):
        source_file_path = os.path.join(source, file_name)

        # Skip directories
        if os.path.isdir(source_file_path):
            continue

        destination_file_path = os.path.join(destination, file_name)

        # If file already exists in destination, add a timestamp
        if os.path.exists(destination_file_path):
            base, ext = os.path.splitext(file_name)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            new_file_name = f"{base}_{timestamp}{ext}"
            destination_file_path = os.path.join(destination, new_file_name)

        try:
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied : {file_name} ==>  ==>  ==> {destination_file_path}")
        except Exception as e:
            print(f"Failed to copy {file_name}: {e}")

if __name__ == "__main__":

    # Check correct number of agruments while running command line
    if len(sys.argv) != 3:
        print("Command should be like: python backup.py /path/to/source /path/to/destination")
    else:
        source_dir = sys.argv[1]
        destination_dir = sys.argv[2]
        backup_files(source_dir, destination_dir)