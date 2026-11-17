from pathlib import Path


def manage_files():
    
    current_dir = Path.cwd()

   
    print("Python files in current directory:")
    for file in current_dir.glob("*.py"):
        if file.is_file():
            print(file.name)

    
    logs_dir = current_dir / "temp_logs"
    logs_dir.mkdir(exist_ok=True)
    print(f"\nChecked/created directory: {logs_dir.name}")



if __name__ == "__main__":
    manage_files()
