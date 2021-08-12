"""Декораторы"""

import sys
import logging
import traceback
import inspect
import os

import progect_logs.configs_logs.config_client_log
import progect_logs.configs_logs.config_server_log

# метод определения модуля, источника запуска.
# Метод find () возвращает индекс первого вхождения искомой подстроки,
# если он найден в данной строке.
# Если его не найдено, - возвращает -1.
print(f'sys.argv[0] = {sys.argv[0]}')
print(f'sys.argv[0] = {os.path.split(sys.argv[0])[1]}')

if sys.argv[0].find('client') == -1:
    # если не клиент то сервер!
    LOGGER = logging.getLogger('server')
else:
    # ну, раз не сервер, то клиент
    LOGGER = logging.getLogger('client')


# Реализация в виде функции
def log(func_to_log):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        """Обертка"""
        ret = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}.' 
                     f'Вызов из функции с помощью traceback {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции с помощью inspect {inspect.stack()[1][3]}',
                     stacklevel=2)
        return ret
    return log_saver


# Реализация в виде класса
class Log:
    """Класс-декоратор"""
    def __call__(self, func_to_log):
        def log_saver(*args, **kwargs):
            """Обертка"""
            ret = func_to_log(*args, **kwargs)
            LOGGER.debug(f'Вызов из класса. Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}.'
                         f'Вызов из модуля {func_to_log.__module__}. Вызов из'
                         f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                         f'Вызов из функции {inspect.stack()[1][3]}',
                         stacklevel=2)
            return ret
        return log_saver
