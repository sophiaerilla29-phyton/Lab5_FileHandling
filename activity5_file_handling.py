from pathlib import Path

student_id = "2025-1234"
student_name = "Sophia Phoebe I. Erilla"

base_dir = Path.cwd() / "Activity_5_Files"
base_dir.mkdir(parents=True, exist_ok=True)

file_path = base_dir / f"intro_{student_id}.txt"

with file_path.open("w", encoding="utf-8") as file:
    file.write(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!")

print(f"File created and text written at: {file_path.resolve()}")

from pathlib import Path

student_id = "2025-1234"

base_dir = Path.cwd() / "Activity_5_Files"
file_path = base_dir / f"intro_{student_id}.txt"

content = file_path.read_text(encoding="utf-8")
print(content)

from pathlib import Path

student_id = "2025-1234"

base_dir = Path.cwd() / "Activity_5_Files"
file_path = base_dir / f"intro_{student_id}.txt"

with file_path.open("a", encoding="utf-8") as file:
    file.write("\nThis is a new line.")

print(f"Line appended to: {file_path.resolve()}")
from pathlib import Path

student_id = "2025-1234"

base_dir = Path.cwd() / "Activity_5_Files"
file_path = base_dir / f"intro_{student_id}.txt"

with file_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

from pathlib import Path
from datetime import datetime
import shutil

student_id = "2025-1234"

base_dir = Path.cwd() / "Activity_5_Files"
base_dir.mkdir(parents=True, exist_ok=True)

def write_with_backup(filename: str, content: str):
    file_path = base_dir / filename

    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = file_path.with_name(
            f"{file_path.stem}_backup_{timestamp}{file_path.suffix}"
        )
        shutil.copy2(file_path, backup_path)
        print(f"Backup saved: {backup_path.name}")

    with file_path.open("w", encoding="utf-8") as file:
        file.write(content)

    print(f"File saved: {file_path.name}")

def read_file(filename: str):
    file_path = base_dir / filename
    with file_path.open("r", encoding="utf-8") as file:
        return file.read()

print("=== File Operations Demo ===")

print("\n1. Creating new file:")
write_with_backup(f"demo_{student_id}.txt", "Initial content")

print("\n2. Updating file (with backup):")
write_with_backup(f"demo_{student_id}.txt", "Updated content")

print("\n3. Reading file:")
print(read_file(f"demo_{student_id}.txt"))

print("\n4. Listing backups:")
for backup in base_dir.glob("*backup*"):
    print("-", backup.name)

from pathlib import Path

student_id = "2025-1234"
student_name = "Sophia Phoebe I. Erilla"

file_path = Path.home() / "Documents" / "Activity_5_Files" / f"lines_{student_id}.txt"

text = file_path.read_text()
word_count = len(text.split())

print(f"{student_name} (ID: {student_id}) - Word count in file '{file_path.name}': {word_count}")