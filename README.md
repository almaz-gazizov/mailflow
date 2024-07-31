#  Mailflow

Mailflow — это инструмент, который позволяет синхронизировать сообщения из различных почтовых сервисов, таких как Yandex, Gmail и Mail.ru. С его помощью вы можете легко импортировать новые сообщения в систему, отслеживать их статус в реальном времени с помощью визуальных индикаторов прогресса и управлять почтовыми аккаунтами через единый интерфейс. 

### Стек используемых технологий:

Python, Django, PostgreSQL, Celery, Redis, WebSocket, Channels, HTML/CSS, JavaScript (jQuery), Git.

## Как развернуть проект

### Клонирование репозитория

1. Клонируйте репозиторий на свой компьютер:
```
git@github.com:almaz-gazizov/mailflow.git
```
2. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
```
3. Установите зависимости проекта:
```
pip install -r requirements.txt
```
4. Создайте файл .env и заполните его своими данными:
```
# Имя пользователя БД
POSTGRES_USER=

# Пароль к БД
POSTGRES_PASSWORD=

# Имя базы данных
POSTGRES_DB=

# Имя Хоста
DB_HOST=

# Порт соединения к БД
DB_PORT=

# Список разрешённых хостов
ALLOWED_HOSTS=

# Режим отладки
DEBUG=
```
5. Выполните миграции и запустите сервер разработки Django:
```
python manage.py migrate
python manage.py runserver
```