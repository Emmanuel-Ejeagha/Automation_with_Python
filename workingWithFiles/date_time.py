from pathlib import Path
from datetime import datetime

base_dir = Path('files')

# Add created date to all the filenames in the folder 
for path in base_dir.glob("**/*"):
    if path.is_file():
        created_date = datetime.fromtimestamp(path.stat().st_ctime)
        created_date_str = created_date.strftime("%Y-%m-%d_%H:%M:%S")
        new_filename = created_date_str + '_' + path.name
        new_filename = path.with_name(new_filename)
        path.rename(new_filename)