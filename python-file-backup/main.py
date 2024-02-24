import os
import shutil
import time
import colorama
import datetime

# Enter the source and destination paths here

source = "C:\\Users\\nik\\Documents\\Code"
destination = "C:\\Users\\nik\\Documents\\Backups"

# Enter the time interval in minutes here

minutes = 1

red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE
reset = colorama.Style.RESET_ALL

colorama.init()

def backupFiles():
    print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {blue} Backing up files...")

    changes = False

    # Creating a backup directory if it doesn't exist

    if not os.path.exists(destination):
       os.makedirs(destination)
       print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {green} Created backup directory {destination}")

    # Deleting files from destination that are not in source
       
    for root, dirs, files in os.walk(destination):
        for file in files:
            file_path = os.path.join(root, file)
            source_file_path = file_path.replace(destination, source)
            if not os.path.exists(source_file_path):
                os.remove(file_path)
                print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {red} Deleted {file_path}")
                changes = True
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            source_dir_path = dir_path.replace(destination, source)
            if not os.path.exists(source_dir_path):
                shutil.rmtree(dir_path)
                print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {red} Deleted {dir_path}")
                changes = True

    # Copying files from source to destination
        
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            destination_file_path = file_path.replace(source, destination)
            if not os.path.exists(destination_file_path) or os.path.getmtime(file_path) != os.path.getmtime(destination_file_path):
                shutil.copy2(file_path, destination_file_path)
                print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {green} Copied {file_path} to {destination_file_path}") 
                changes = True
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            destination_dir_path = dir_path.replace(source, destination)
            if not os.path.exists(destination_dir_path):
                os.makedirs(destination_dir_path)   
                print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {green} Created {destination_dir_path}")
                changes = True

    if changes:
        print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {blue} Changes detected. Backup complete")
    else:
        print(f"{reset} [{datetime.datetime.now().strftime('%H:%M:%S')}] {blue} No changes detected. Backup complete")

while True:
    backupFiles()
    time.sleep(60 * minutes)