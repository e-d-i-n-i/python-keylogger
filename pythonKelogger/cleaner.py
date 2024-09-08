import os
import shutil

# Path to the Prefetch folder (Windows specific)
prefetch_dir = r"C:\Windows\Prefetch"

def clean_prefetch():
    """Deletes all files from the Windows Prefetch folder."""
    if os.path.exists(prefetch_dir):
        try:
            for file_name in os.listdir(prefetch_dir):
                file_path = os.path.join(prefetch_dir, file_name)

                # Check if it's a file and not a directory
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                elif os.path.isdir(file_path):
                    # Rare case, but handle if there are sub-directories
                    shutil.rmtree(file_path)
                    print(f"Deleted directory: {file_path}")
            print("Prefetch folder cleared successfully.")
        except Exception as e:
            print(f"An error occurred while clearing Prefetch: {e}")
    else:
        print(f"Prefetch folder '{prefetch_dir}' does not exist.")

def delete_syshelper_logs():
    """Delete only the files named 'SysHelper'."""
    log_dir = os.getcwd()  # Current working directory
    files_to_delete = [f for f in os.listdir(log_dir) if 'SysHelper' in f]

    # Delete all files that contain 'SysHelper' in their name
    for file_name in files_to_delete:
        file_path = os.path.join(log_dir, file_name)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"An error occurred while deleting {file_name}: {e}")

def full_cleanup():
    """Performs a full clean-up: removes Prefetch files and 'SysHelper' logs."""
    clean_prefetch()
    delete_syshelper_logs()

if __name__ == "__main__":
    full_cleanup()
