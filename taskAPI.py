# Напишите функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки. https://api.thecatapi.com/v1/images/search
# Напишите тест, который проверяет успешный запрос и возвращает правильный URL.
# Напишите тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.

import requests

def get_random_cat_image():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        return response.json()[0]["url"]
    else:
        return None

print(get_random_cat_image())