#Write a file-reader utility safe_json_read(file_path: str) -> dict that attempts to open
#open and load a JSON file.
# Use try/except to catch FileNotFoundError and json.JSONDecodeError.
# Use the else block to return the parsed payload,
# and a finally block to print "Execution completed for [file_path]".
import json

def safe_json_read(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
        
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return {}
        
    else:
        return data
        
    finally:
        print(f"Execution completed for {file_path}")


with open("valid.json", "w") as f:
    json.dump({"student": "Alice", "score": 95}, f)


with open("broken.json", "w") as f:
    f.write('{"student": "Bob", "score": ')

test_files = ["valid.json", "broken.json", "missing.json"]

for path in test_files:
    print(f"--- Testing: {path} ---")
    result = safe_json_read(path)
    print(f"Returned: {result}\n")
