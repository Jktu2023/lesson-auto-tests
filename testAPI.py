
# Напишите тест, который проверяет успешный запрос и возвращает правильный URL.
# Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.

import pytest
from taskAPI import get_random_cat_image

def test_get_random_cat_image(mocker):
    mock.get = mocker.patch('taskAPI.requests.get')
    mock.get.return_value.status_code = 200
    mock.get.return_value.json.return_value = [{"url": "https://example.com/cat.jpg"}]