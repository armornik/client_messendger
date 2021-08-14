"""Лаунчер"""

import subprocess

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    # Команда для выхода
    if ACTION == 'q':
        break
    elif ACTION == 's':
        # Запускаем сервер по команде
        PROCESS.append(subprocess.Popen('python server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        # Создаём двух клиентов, которые посылают сообщение -m - режим mode
        for i in range(2):
            PROCESS.append(subprocess.Popen('python client.py -m send',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
        # Создаём 5 клиентов, которые получают сообщения
        for i in range(5):
            PROCESS.append(subprocess.Popen('python client.py -m listen',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    # Команда для закрытия окон
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
