import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, "files")
ZIP_DIR = os.path.join(FILES_DIR, "zip_test.zip")
print(ZIP_DIR)
