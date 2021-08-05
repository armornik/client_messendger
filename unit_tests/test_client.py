""" Unit-тесты клиента """
import sys
import os
import unittest

from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, HELLO
from client import create_presence, process_ans

# Получаем относительный путь
sys.path.append(os.path.join(os.getcwd(), '..'))


class TestClass(unittest.TestCase):
    """ Класс с тестами """

    def test_def_presence(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
        # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_def_not_presence(self):
        """Тест ошибочного запроса"""
        test = create_presence()
        test[TIME] = 1.2  # время необходимо приравнять принудительно
        # иначе тест никогда не будет пройден
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректного разбора ответа 200"""
        self.assertEqual(process_ans({RESPONSE: 200, HELLO: 'Hello, Guest'}), ('Hello, Guest', '200 : OK'))

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(process_ans({RESPONSE: 400, HELLO: 'Hello, Guest', ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
