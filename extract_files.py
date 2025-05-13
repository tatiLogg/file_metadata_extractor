import os

def extract_file_info_nested(path='.'):
    """
    Recursively collects file information and organizes it in a nested dictionary.
    Keys are folder paths, and values are dictionaries of {filename: {path, size}}.
    """
    nested_info = {}

    for root, _, files in os.walk(path):
        relative_root = os.path.relpath(root, path)
        nested_info[relative_root] = {}

        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)
            nested_info[relative_root][file] = {
                'path': full_path,
                'size': size
            }

    return nested_info

# Test the function
if __name__ == "__main__":
    nested = extract_file_info_nested()
    from pprint import pprint
    pprint(nested)

