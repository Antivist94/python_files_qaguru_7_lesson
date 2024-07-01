import os
import shutil
import pytest
import zipfile
from .test_data import get_example_file_from_resource, pdf_resource, csv_resource, xlsx_resource
from script_os import FILES_DIR


@pytest.fixture(scope = "session", autouse = True)
def precondition_get_files_and_create_archive_with_files():
    # Проверка на наличие папки с файлами - если нет папки, создается папка с файлами
    if not os.path.exists(FILES_DIR):
        os.mkdir(FILES_DIR)
    # Загрузка файлов для теста
    get_example_file_from_resource(pdf_resource, "pdf_example.pdf")
    get_example_file_from_resource(xlsx_resource, "xlsx_example.xlsx")
    get_example_file_from_resource(csv_resource, "csv_example.csv")
    file_list = ["pdf_example.pdf", "xlsx_example.xlsx", "csv_example.csv"]
    # Создание пустого архива
    new_zip_file = os.path.join(FILES_DIR, 'zip_test.zip')
    with zipfile.ZipFile(new_zip_file, 'w') as new_zip:
        pass
    # Добавление файлов в архив
    with zipfile.ZipFile(new_zip_file, 'a') as upd_zip:
        for file in file_list:
            file_path = os.path.join(FILES_DIR, file)
            upd_zip.write(file_path, os.path.basename(file_path))
    print("Архив с файлами создан")

    yield
    shutil.rmtree(FILES_DIR)
