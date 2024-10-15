from pathlib import Path

base_dir = Path("rename/Jan")

# Change file extentions
for path in base_dir.rglob("*.txt"):
# for path in base_dir.glob("*.txt"):
# for path in base_dir.rglob("*"):  # this also works, rglob is used when you have subfolder
    if path.is_file():
        new_filepath = path.with_suffix(".csv")
        path.rename(new_filepath)