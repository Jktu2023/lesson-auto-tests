
# Напишите тест, который проверяет успешный запрос и возвращает правильный URL.
# Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.

import pytest
from taskAPI import get_random_cat_image

def test_get_random_cat_image(mocker):
    mock_get = mocker.patch('taskAPI.requests.get') # Подменить реальный вызов requests.get() на «заглушку» (мок), чтобы не делать настоящий HTTP-запрос во время теста.
    mock_get.return_value.status_code = 200 # "настраивает" мок-объект так, чтобы при вызове requests.get(...) он возвращал объект, у которого атрибут status_code равен 200.
                                        # то есть «Когда функция get_random_cat_image() вызовет requests.get(...), пусть ей "пришлют" ответ с HTTP-статусом 200 (успех)».
    mock_get.return_value.json.return_value = [{"url": "https://example.com/cat.jpg"}] # «Сделай так, чтобы при вызове response.json() (где response — результат requests.get) возвращался именно этот список с URL, включая все пробелы».

    result = get_random_cat_image() # получить случайное изображение кошки
    assert result == "https://example.com/cat.jpg" # проверить, что результат соответствует ожидаемому

    # mock_get.return_value.status_code = 404
    # result = get_random_cat_image()
    # assert result is None

def test_get_random_cat_image_error(mocker):
    mock_get = mocker.patch('taskAPI.requests.get')
    mock_get.return_value.status_code = 500

    result = get_random_cat_image()
    assert result is None

