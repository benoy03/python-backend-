import os
import shutil
import datetime
import argparse
import json
import logging
import mimetypes
from concurrent.futures import ThreadPoolExecutor

# -----------------------------
# Default Rules
# -----------------------------
DEFAULT_RULES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

# -----------------------------
# Logging Setup
# -----------------------------
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -----------------------------
# Utility Functions
# -----------------------------
def load_rules(config_file=None):
    if config_file and os.path.isfile(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    return DEFAULT_RULES

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Created folder: {path}")

def get_date_folder(file_path, date_type="modification"):
    timestamp = os.path.getmtime(file_path) if date_type=="modification" else os.path.getctime(file_path)
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%Y-%m")

def safe_move(src, dest, dry_run=False):
    """Move file safely, avoid overwriting."""
    create_folder(dest)
    base_name = os.path.basename(src)
    dest_path = os.path.join(dest, base_name)
    counter = 1
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(base_name)
        dest_path = os.path.join(dest, f"{name}({counter}){ext}")
        counter += 1
    if dry_run:
        print(f"[DRY RUN] Would move: {src} -> {dest_path}")
    else:
        shutil.move(src, dest_path)
        logging.info(f"Moved: {src} -> {dest_path}")
        print(f"Moved: {src} -> {dest_path}")

def detect_folder_by_mime(file_path, rules):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        for folder, extensions in rules.items():
            if any(file_path.lower().endswith(ext) for ext in extensions):
                return folder
    return "Others"

# -----------------------------
# File Organizer
# -----------------------------
def organize_file(entry, directory, rules, by_date=False, date_type="modification", dry_run=False):
    if not entry.is_file():
        return None
    moved = False
    for folder, extensions in rules.items():
        if entry.name.lower().endswith(tuple(extensions)):
            dest_folder = os.path.join(directory, folder)
            if by_date:
                dest_folder = os.path.join(dest_folder, get_date_folder(entry.path, date_type))
            safe_move(entry.path, dest_folder, dry_run)
            moved = True
            break
    if not moved:
        dest_folder = os.path.join(directory, "Others")
        if by_date:
            dest_folder = os.path.join(dest_folder, get_date_folder(entry.path, date_type))
        safe_move(entry.path, dest_folder, dry_run)

def organize_directory(directory, rules, by_date=False, date_type="modification", dry_run=False):
    entries = list(os.scandir(directory))
    with ThreadPoolExecutor() as executor:
        for entry in entries:
            executor.submit(organize_file, entry, directory, rules, by_date, date_type, dry_run)

# -----------------------------
# Main
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Advanced Automated File Organizer")
    parser.add_argument("directory", nargs="?", help="Directory to organize")
    parser.add_argument("--config", help="Path to JSON config file", default=None)
    parser.add_argument("--by-date", help="Organize files by date", action="store_true")
    parser.add_argument("--date-type", choices=["creation", "modification"], default="modification", help="Use creation or modification date")
    parser.add_argument("--dry-run", help="Simulate actions without moving files", action="store_true")
    
    args = parser.parse_args()
    
    # Interactive prompt if directory not given
    if not args.directory:
        args.directory = input("Enter directory to organize: ").strip()
    
    if not os.path.isdir(args.directory):
        print("Error: Provided path is not a directory.")
        return
    
    rules = load_rules(args.config)
    organize_directory(args.directory, rules, by_date=args.by_date, date_type=args.date_type, dry_run=args.dry_run)
    print("Organization complete!")

if __name__ == "__main__":
    main()
