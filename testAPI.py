
# Напишите тест, который проверяет успешный запрос и возвращает правильный URL.
# Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.

import pytest
from taskAPI import get_random_cat_image

def test_get_random_cat_image(mocker):
    mock_get = mocker.patch('taskAPI.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"url": "https://example.com/cat.jpg"}]

    result = get_random_cat_image()
    assert result == "https://example.com/cat.jpg"

    # mock_get.return_value.status_code = 404
    # result = get_random_cat_image()
    # assert result is None

def test_get_random_cat_image_error(mocker):
    mock_get = mocker.patch('taskAPI.requests.get')
    mock_get.return_value.status_code = 500

    result = get_random_cat_image()
    assert result is None

