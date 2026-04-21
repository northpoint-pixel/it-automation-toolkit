import os

LOG_FOLDER = os.path.expanduser("~/Downloads")

def delete_temp_logs(folder_path):
    deleted_count = 0

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".log") or file_name.endswith(".tmp"):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted_count += 1
                print(f"Deleted: {file_name}")

    print(f"\nTotal files deleted: {deleted_count}")

if __name__ == "__main__":
    delete_temp_logs(LOG_FOLDER)