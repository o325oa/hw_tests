from main import longest_film
from main import list_of_numbers
from main import solve
import unittest


# 1 тест проверяет что возвращает правильное название

class TestLongestFilm(unittest.TestCase):
    def test_longest_film(self):
        self.assertEqual(longest_film('Аладин', 'Мадагаскар', 'Бетховен'), 'Мадагаскар')


# 2 тест проверяет что функция возвращает правильный список чисел

class TestListOfNumbers(unittest.TestCase):
    def test_list_of_numbers(self):
        self.assertEqual(list_of_numbers(5), [1, 2, 3, 4, 5])


# 3 тест проверяет, что черепаха выиграла

class TestRace(unittest.TestCase):
    def test_turtle_wins(self):
        result = solve([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3])
        self.assertEqual(result, "черепаха", f"Победитель определен неверно: {result}")
