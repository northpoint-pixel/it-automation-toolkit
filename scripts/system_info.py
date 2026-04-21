import platform
import socket
import os

def get_system_info():
    print("System Information")
    print("-" * 30)
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Current User: {os.getlogin()}")

if __name__ == "__main__":
    get_system_info()