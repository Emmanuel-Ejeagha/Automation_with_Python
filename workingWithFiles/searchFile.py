from pathlib import Path

base_dir = Path('.')
search_value = '14'

for path in base_dir.rglob("*"):
    if search_value in path.stem:
        print(path.absolute())