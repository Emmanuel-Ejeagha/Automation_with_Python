from pathlib import Path
import zipfile

base_dir = Path("createEmptyFiles")
archive_path = base_dir / Path('files.zip')

# zip files
with zipfile.ZipFile(archive_path, 'w') as Zfile:
    for path in base_dir.rglob("*.txt"):
        Zfile.write(path)
        
#     # unzip files
# with zipfile.ZipFile(archive_path, 'r') as Zfile:
#     for path in base_dir.rglob("*.txt"):
#         Zfile.write(path)