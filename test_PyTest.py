import pytest
from task_PyTest import count_vowels

@pytest.mark.parametrize("number, expected", [
   ('hello', 2),
   ('apache', 3),
   ('scktch', 0),
   ('Грозный', 2),
   ('Площадь революции', 7),
   ('Молчалин - герой нашего времени', 11), ])

def test_check(number, expected):
   assert count_vowels(number) == expected