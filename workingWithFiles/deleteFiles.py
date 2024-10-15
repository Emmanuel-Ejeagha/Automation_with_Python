from pathlib import Path

base_dir = Path('files')

for path in base_dir.glob("*.txt"):
    with open(path, 'wb') as file:
        file.write(b"")
    path.unlink()