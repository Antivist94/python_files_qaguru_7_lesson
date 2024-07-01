import os.path
import requests
from script_os import FILES_DIR

pdf_resource = "https://file-examples.com/storage/feda9677416682bc7a229d1/2017/10/file-sample_150kB.pdf"
xlsx_resource = "https://file-examples.com/storage/feda9677416682bc7a229d1/2017/02/file_example_XLSX_10.xlsx"
csv_resource = "https://file-examples.com/storage/feda9677416682bc7a229d1/2017/02/file_example_CSV_5000.csv"


def get_example_file_from_resource(get_file_link, filename):
    response = requests.get(get_file_link)
    if response.status_code == 200:
        file_path = os.path.join(FILES_DIR, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("Файл успешно загружен")
    else:
        print("Произошла ошибка при загрузке файла")
