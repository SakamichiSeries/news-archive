import os

folder_path = '.'

for filename in os.listdir(folder_path):
    if filename.endswith('.1'):
        new_name = filename[0].upper() + filename[1:].replace('.1', '')
        os.rename(
            os.path.join(folder_path, filename),
            os.path.join(folder_path, new_name)
        )
        print(f'Renamed: {filename} -> {new_name}')