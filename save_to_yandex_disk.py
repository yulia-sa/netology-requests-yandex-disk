import os
import requests


API_UPLOAD = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл на Яндекс.Диск"""
        self.file_path = file_path

        headers = {
            'Authorization': "OAuth " + self.token
        }

        with open(self.file_path, "rb") as f:
            file_name = os.path.basename(self.file_path)

            try:
                resource_for_upload = requests.get(API_UPLOAD, headers=headers, params={"path": file_name}).json()
                requests.put(resource_for_upload["href"], headers=headers, files={"file": f})
                return f"Файл {file_name} успешно загружен!"
            except KeyError:
                return f"Ошибка!\n{resource_for_upload}"


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "put_your_path_here"
    token = "put_your_token_here"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
