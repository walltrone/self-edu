import requests

HTTP_STATUS_CREATE: int = 201


class YaUploader:
    URL_UPLOAD_LINK: str = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_files_list(self):
        response = requests.get(self.URL_FILES_LIST, headers=self.header)
        return response.json()

    def _get_upload_link(self, ya_disk_path: str):
        params = {"path": ya_disk_path, "overwrite": "true"}
        response = requests.get(self.URL_UPLOAD_LINK, headers=self.header, params=params)
        upload_url = response.json().get("href")
        return upload_url

    def upload(self, path_to_file: str):
        if '/' in path_to_file:
            ya_disk_path = path_to_file.split('/')[-1]
        elif f'\\' in path_to_file:
            ya_disk_path = path_to_file.split('\\')[-1]
        upload_link = self._get_upload_link(ya_disk_path)
        with open(path_to_file, 'rb') as file_obj:
            response = requests.put(upload_link, data=file_obj)
            if response.status_code == HTTP_STATUS_CREATE:
                print(f'Файл {ya_disk_path} успешно загружен')
        return response.status_code


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите полный путь файла')
    token = input('Введите token')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
