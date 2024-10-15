# from pathlib import Path
# import zipfile

# base_dir = Path('./')
# destination_path = Path('extractFiles')

# for path in base_dir.rglob("*.zip"):
#     with zipfile.ZipFile(path, 'r') as zipF:
#         final_path = destination_path / Path(path.stem)
#         zipF.extractall(path=final_path)

from pathlib import Path
import zipfile

# Define the base directory and destination path
base_dir = Path('.')
destination_path = Path('extractFiles')

# Create the destination directory if it doesn't exist
# destination_path.mkdir(exist_ok=True)

# Iterate through all ZIP files in the base directory
for path in base_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        # Create a final path for extraction
        final_path = destination_path / Path(path.stem)
        
        # Create the final path directory if it doesn't exist
        # final_path.mkdir(exist_ok=True)
        
        # Extract all contents to the final path
        zf.extractall(path=final_path)
        print("Done")


# NWKN