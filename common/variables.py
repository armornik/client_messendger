"""Константы"""

import logging

# Порт по умолчанию для сетевого ваимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'
# Текущий уровень логирования (будут сохраняться все сообщения от уровня DEBUG и выше)
LOGGING_LEVEL = logging.DEBUG

# Прококол JIM основные ключи:
ACCOUNT_NAME = 'account_name'
ACTION = 'action'
DESTINATION = 'to'
HELLO = 'Hello'
SENDER = 'sender'
TIME = 'time'
USER = 'user'


# Прочие ключи, используемые в протоколе
ERROR = 'error'
EXIT = 'exit'
PRESENCE = 'presence'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
RESPONSE = 'response'
RESPONSE_200 = {RESPONSE: 200}
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
