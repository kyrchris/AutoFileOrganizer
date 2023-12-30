from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import shutil

#Handler to observe folder to track
class MyHandler(FileSystemEventHandler):
    def create_destination_folder(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename not in ['New Items', '.DS_Store']:
                new_name = filename
                file_extension = os.path.splitext(new_name)[1].lstrip(".")

                # Define folder destinations
                destination_folders = {
                    "xlsx": "/Users/user/Desktop/New Items/Excel files",
                    "doc": "/Users/user/Desktop/New Items/Word files",
                    "docx": "/Users/user/Desktop/New Items/Word files",
                    "pdf": "/Users/user/Desktop/New Items/PDF files",
                    "app": "/Users/user/Desktop/New Items/Applications",
                    "jpg": "/Users/user/Desktop/New Items/Pictures",
                    "R": "/Users/user/Desktop/New Items/R files",
                    "": "/Users/user/Desktop/New Items/Other Folders",
                    "zip": "/Users/user/Desktop/New Items/Zip files",
                }

                # Set the default destination folder
                folder_destination = "/Users/user/Desktop/New Items"

                # Check if a specific folder destination is defined for the file extension
                if file_extension in destination_folders:
                    folder_destination = destination_folders[file_extension]

                # Create the destination folder if it does not exist
                self.create_destination_folder(folder_destination)

                # Ensure unique file names in the destination folder
                i = 1
                file_exists = os.path.isfile(os.path.join(folder_destination, new_name))
                while file_exists:
                    i += 1
                    base_name, extension = os.path.splitext(new_name)
                    new_name = f"{base_name}_{i}{extension}"
                    file_exists = os.path.isfile(os.path.join(folder_destination, new_name))

                # Move the file to the destination folder
                src = os.path.join(folder_to_track, filename)
                new_name = os.path.join(folder_destination, new_name)
                print(f"A new file has been Downloaded with an extension: {file_extension}")
                os.rename(src, new_name)


# Specify the source and destination folders
folder_to_track = "/Users/user/Downloads"
folder_destination = "/Users/user/Desktop/New Items"

# Set up the observer and event handler
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
