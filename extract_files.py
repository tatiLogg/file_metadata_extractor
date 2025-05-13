import os

files_info = []

for file_name in os.listdir():
    if os.path.isfile(file_name):
        file_size = os.path.getsize(file_name)
        files_info.append({'path': file_name, 'size': file_size})

print(files_info)

