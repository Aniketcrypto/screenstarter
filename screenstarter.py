import os
import subprocess

# Get the current directory
base_dir = os.getcwd()

# Function to create a new screen session and run a command
def create_screen_and_run(folder_name):
    screen_name = f"screen_{folder_name}"
    command = f"screen -dmS {screen_name} bash -c 'cd {os.path.join(base_dir, folder_name)} && python3 nodepay.py; exec bash'"
    subprocess.run(command, shell=True)
    print(f"Created screen session '{screen_name}' and started nodepay script in folder '{folder_name}'")

# Get the list of all directories in the current directory
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        create_screen_and_run(folder)

print("All screens have been created and scripts started.")
