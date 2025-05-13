import os

def extract_file_info(path='.'):
    """
    Recursively collects file information starting from the given path.
    Returns a list of dictionaries with file path and size.
    """
    files_info = []

    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)
            files_info.append({'path': full_path, 'size': size})

    return files_info

# Test the function
if __name__ == "__main__":
    results = extract_file_info()
    for item in results:
        print(item)


