from pathlib import Path

base_dir = Path('testing')

# rename all file based on sub-sub-folders
for path in base_dir.glob("**/*"):
    if path.is_file():
        p_folder = path.parts
        print(p_folder)
        subfolders = path.parts[1:-1]
        
        new_filename = "-".join(subfolders) + '-' + path.name
        print(new_filename)
        new_filename = path.with_name(new_filename)
        path.rename(new_filename)
        