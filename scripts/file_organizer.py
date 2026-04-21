import os
import shutil

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Installers": [".msi", ".exe"],
    "Code": [".py", ".js", ".html", ".css", ".java"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)
        moved = False

        for category, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                destination = os.path.join(category_folder, file_name)
                shutil.move(file_path, destination)
                print(f"Moved: {file_name} -> {category}/")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Other")
            os.makedirs(other_folder, exist_ok=True)
            destination = os.path.join(other_folder, file_name)
            shutil.move(file_path, destination)
            print(f"Moved: {file_name} -> Other/")

if __name__ == "__main__":
    organize_files(DOWNLOADS_FOLDER)