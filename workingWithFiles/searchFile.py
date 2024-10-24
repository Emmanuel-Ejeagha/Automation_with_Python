from pathlib import Path

base_dir = Path('.')
search_value = '14'

# search for a file in a dir
for path in base_dir.rglob("*"):
    if path.is_file():
        if search_value in path.stem:
            print(path.absolute())