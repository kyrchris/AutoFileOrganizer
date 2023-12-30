# AutoFileOrganizer

## Overview

AutoFileOrganizer is a Python script designed to automate the organization and cleanup of the user's Downloads folder. The script utilizes the `watchdog` library to monitor changes in the specified folder, intelligently categorizing and moving files to destination folders based on their types or extensions.

## Features

- **Automatic File Categorization:** The script dynamically categorizes files into specific folders based on their file types or extensions.

- **Destination Folder Creation:** If destination folders for specific file types do not exist, the script creates them automatically.

- **File Naming:** The script ensures unique file names in destination folders to prevent naming conflicts.

- **Real-time Monitoring:** Changes to the Downloads folder are monitored in real-time, triggering the categorization process as soon as a file is modified.

## Usage

1. **Installation:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using `pip install watchdog`.

2. **Configuration:**
   - Set the `folder_to_track` variable in the script to the path of your Downloads folder.
   - Adjust the `folder_destination` variable to set the root destination folder.

3. **Run the Script:**
   - Execute the script by running `python your_script_name.py` in the terminal.

4. **Customization:**
   - Customize the `destination_folders` dictionary in the script to define specific folders for additional file types.

## Acknowledgments

This script was inspired by and adapted from a tutorial on [YouTube](link-to-the-youtube-video](https://www.youtube.com/watch?v=HcZ3gS1Rgcs&t=721s)).

