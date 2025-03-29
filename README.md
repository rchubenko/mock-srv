# Mock Server

Mock Server — это простой сервер, разработанный на Python с использованием библиотеки Flask, предназначенный для эмуляции API эндпоинтов в процессе разработки и тестирования приложений.

## Начало работы

### Предварительные требования

- [Python 3.x](https://www.python.org/downloads/): убедитесь, что Python установлен на вашей системе.
- [pip](https://pip.pypa.io/en/stable/installation/): менеджер пакетов Python.

### Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/rchubenko/mock-srv.git
   cd mock-srv
   ```

2. **Создайте виртуальное окружение (рекомендуется):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Запустите сервер:**
   ```bash
   python mock_server.py
   ```

   После выполнения этих шагов сервер будет доступен по адресу `http://localhost:5000`.

## Структура проекта

- `mock_server.py`: основной файл сервера на Flask.
- `requirements.txt`: список зависимостей проекта.
- `Dockerfile`: инструкция для создания Docker-образа.

## Docker

Для контейнеризации приложения используется `Dockerfile`. Чтобы собрать и запустить Docker-контейнер:

1. **Соберите Docker-образ:**
   ```bash
   docker build -t mock-srv .
   ```

2. **Запустите контейнер:**
   ```bash
   docker run -p 5000:5000 mock-srv
   ```

   После этого сервер будет доступен по адресу `http://localhost:5000`.
