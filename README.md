Этот сайт написан на Django(Python). Так же использовался Vite (django-vite) и SCSS.

## Для запуска сайта (в режиме разработки), требуется установить зависимости:
1. Python не выше 3.11
2. pipenv или virtualvenv(python3-venv)
3. Пакетный менеджер pip
3. Node.js

## Установка зависимостей Python:
1. Для начала необходимо создать виртуальное окружение:
### Linux
#### Если стоит pipenv:
```bash
pipenv shell
```
После того, как pipenv создал виртуальное окружение и вошёл в него, следует установить зависимости:
```bash
pipenv install
```
#### Если стоит venv
Создаём окружение:
```bash
python3 -m venv venv
```
Входим в окружение:
```bash
source venv/bin/activate # Следите в какой вы директории
```
Установить зависимости можно из файла req.txt
```bash
pip3 install -r req.txt
```
### Windows
#### Если стоит pipenv:
На Windows лучше будет сразу установить зависимости (он сразу же создаст окружение):
```bash
py -m pipenv install
```
После этого, мы можем войти в окружение:
```bash
py -m pipenv shell
```
#### Если стоит venv
Создаём окружение:
```bash
py -m venv venv
```
Входим в окружение:
```bash
venv\Scripts\activate.bat # Следите в какой вы директории
```
Установить зависимости можно из файла req.txt
```bash
pip install -r req.txt
```

##### Проверка работоспособности:
Для того чтобы проверить работоспособность, можем запустить локальный сервер:
### Linux
```bash
python3 manage.py runserver
```
### Windows
```bash
py -m pipenv run py manage.py runserver
```
ИЛИ, можете перейти в виртуальное окружение:
```bash
py -m pipenv shell
```
А там, уже запустить локальный сервер:
```bash
py manage.py runserver
```
# **ВНИМАНИЕ**
После этого, разделения на ОС не будет, будьте внимательны

## Миграции
После установки зависимостей, следует создать миграции:
```bash
python manage.py makemigrations RegAuth main news products
python manage.py makemigrations # На всякий случай
```
Далее необходимо эти миграции мигрировать
```bash
python manage.py migrate
```

## Установка зависимостей Node
Установка зависимостей Node не отличается между ОС.
Переходите в рабочую директорию и вводите:
```bash
npm install
```

## Запуск проекта
Запуск Django
```bash
python manage.py runserver
```
Запуск Vite сервера
```bash
npx vite
```
ИЛИ
```bash
npm run dev
```
### Создание администратора (работает только с non_email_register)
Для создания администратора, введите:
```bash
python manage.py createsuperuser
```
Вводите что просит система

Если лень разворачивать: http://dadamapt.beget.tech (может быть уже заблокирован)
