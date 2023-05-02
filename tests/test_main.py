from main import YaUploader
from unittest import TestCase
import requests

ya_token = input('Введите корректный токен')

class TestYaUploader(TestCase):

    def test_correct(self):
        ya = YaUploader(ya_token)
        result = ya.create_folder('/тест1')
        expected = 201
        self.assertEqual(result, expected)

    def test_correct2(self):
        ya = YaUploader(ya_token)
        ya.create_folder('/тест2')
        url = 'https://disk.yandex.ru/client/disk/тест1'
        response = requests.get(url)
        expected = 200
        self.assertEqual(response.status_code, expected)

    def test_not_correct_token(self):
        ya = YaUploader(ya_token+'i')
        result = ya.create_folder('/тест2')
        expected = 401
        self.assertEqual(result, expected)

    def test_folder_exists(self):
        ya = YaUploader(ya_token)
        result = ya.create_folder('/тест1')
        expected = 409
        self.assertEqual(result, expected)

