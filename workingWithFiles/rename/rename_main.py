from pathlib import Path

base_dir = Path('rename')
file_paths = base_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + '_' + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)