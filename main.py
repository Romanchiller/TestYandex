import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return { 'Content-Type': 'application/json',
                 'Authorization': 'OAuth {}'.format(self.token)}


    def create_folder(self, folder_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_path}
        response = requests.put(url=url, params=params, headers=headers)
        if response.status_code == 201:
            return response.status_code
        else: return response.status_code



