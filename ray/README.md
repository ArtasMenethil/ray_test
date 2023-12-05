# Back-End
Программа автоматически стягивает новости с newsapi.org и помещает в БД. Записи можно просматривать, редактировать и 
удалять.


## Установка зависимостей

```commandline
pip install -r requirements.txt
```

## Переменные окружения
Список ожидаемых переменных окружения, используемых сервисом, описан в файле .env.example.
По аналогии с ним необходимо настроить файл .env. Для этого нужно скопировать файл
.env.example под именем .env и настроить переменные окружения:
```commandline
cp .env.example .env
```

## Описание переменных окружения

### DJANGO_SECRET_KEY
Секреиный ключ

### DB_ENGINE
URL строка подключения к БД
(как вариант django.db.backends.postgresql_psycopg2)

### POSTGRES_USER
Пользователь БД

### POSTGRES_DB
Имя БД

### POSTGRES_PASSWORD
Пароль БД

### POSTGRES_PORT
Порт для подключения к БД

### POSTGRES_HOST
Хост БД (для локального подключения localhost)

### REDIS_HOST
Хост Redis (localhost)

### REDIS_PORT
Порт default=6379


## Подготовка к запуску

Создать админа 

```commandline
python manage.py createsuperuser
```

Провести миграции

```commandline
python manage.py makemigration
```
```commandline
python manage.py migrate
```

## Запуск сервера

```commandline
python manage.py runserver
```

## Запуск Celery
Для автоматического пополнения БД в заданное время запустить celery задачу командой
```commandline
celery -A ray worker --loglevel=info
```
задача будет выполняться асинхронно