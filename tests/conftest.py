import os
import shutil
import pytest
import zipfile
from script_os import ARCHIVE_DIR, ZIP_DIR, FILES_DIR


@pytest.fixture(scope = "session", autouse = True)
def precondition_get_files_and_create_archive_with_files():
    # Проверка на наличие папки с архивом - если нет папки, создается папка с архивом
    if not os.path.exists(ARCHIVE_DIR):
        os.mkdir(ARCHIVE_DIR)
    # Указание файлов для теста
    file_list = ["pdf_example.pdf", "xlsx_example.xlsx", "csv_example.csv"]
    # Создание пустого архива
    new_zip_file = os.path.join(ARCHIVE_DIR, 'zip_test.zip')
    with zipfile.ZipFile(new_zip_file, 'w') as new_zip:
        pass
    # Добавление файлов в архив
    with zipfile.ZipFile(new_zip_file, 'a') as upd_zip:
        for file in file_list:
            file_path = os.path.join(FILES_DIR, file)
            upd_zip.write(file_path, os.path.basename(file_path))

    yield
    shutil.rmtree(ARCHIVE_DIR)
