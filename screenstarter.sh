#!/bin/bash

# Get the current directory
base_dir=$(pwd)

# Loop through all directories in the current directory
for folder in "$base_dir"/*; do
    if [ -d "$folder" ]; then
        folder_name=$(basename "$folder")
        
        # Create a new screen session and run the nodepay script inside that folder
        screen_name="screen_$folder_name"
        screen -dmS "$screen_name" bash -c "cd '$folder' && python3 nodepay.py; exec bash"
        
        echo "Created screen session '$screen_name' and started nodepay script in folder '$folder_name'"
    fi
done

echo "All screens have been created and scripts started."
