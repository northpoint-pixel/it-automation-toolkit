import shutil

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)

    print("Disk Usage Report")
    print("-" * 30)
    print(f"Total: {total // (1024**3)} GB")
    print(f"Used:  {used // (1024**3)} GB")
    print(f"Free:  {free // (1024**3)} GB")

if __name__ == "__main__":
    check_disk_usage("C:\\")