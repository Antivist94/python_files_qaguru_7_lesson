import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, "files")
ARCHIVE_DIR = os.path.join(CURRENT_DIR, "archive")
ZIP_DIR = os.path.join(ARCHIVE_DIR, "zip_test.zip")
