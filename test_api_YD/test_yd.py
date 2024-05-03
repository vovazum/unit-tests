import requests
import pytest

def create_folder(folder_name):
    # Предположим, что у нас есть функция для создания папки на Яндекс.Диске
    # Она должна отправлять POST запрос на URL с заголовком Authorization и телом запроса, содержащим название папки
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    }
    data = {
        "path": f"/{folder_name}",
    }
    response = requests.post(url, headers=headers, data=data)
    return response

def test_create_folder_success():
    # Проверяем успешное создание папки
    response = create_folder("TestFolder")
    assert response.status_code == 201  # Проверяем код ответа
    # Дополнительные проверки, например, что папка действительно создана
    # Это зависит от того, как устроено API Яндекс.Диска и какие данные возвращает успешный запрос

@pytest.mark.parametrize("folder_name", ["", "Test Folder", "Тестовая_папка"])
def test_create_folder_invalid_name(folder_name):
    # Проверяем случаи с некорректными названиями папок
    response = create_folder(folder_name)
    assert response.status_code == 400  # Ожидаем ошибку 400 Bad Request

def test_create_folder_unauthorized():
    # Проверяем случай, когда запрос выполняется без авторизации
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    response = requests.post(url)
    assert response.status_code == 401  # Ожидаем ошибку 401 Unauthorized