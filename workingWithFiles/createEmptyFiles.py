from pathlib import Path

base_dir = Path("createEmptyFiles")

#  creates an empty files
for i in range(10, 20):
    filename = str(i) + '.csv'
    filepath = base_dir / Path(filename)
    filepath.touch()