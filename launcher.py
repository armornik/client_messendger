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
        # Создаём клиентов

        PROCESS.append(subprocess.Popen('python client.py -n client_1',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))

        PROCESS.append(subprocess.Popen('python client.py -n client_2',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESS.append(subprocess.Popen('python client.py -n client_3',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESS.append(subprocess.Popen('python client.py -n client_4',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESS.append(subprocess.Popen('python client.py -n client_5',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
    # Команда для закрытия окон
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
