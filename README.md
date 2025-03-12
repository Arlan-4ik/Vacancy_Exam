"vacancy_project"

# 📌 Проект на Django с Djongo (MongoDB)

## 📖 Описание

Этот проект использует **Django** 

## 🚀 Установка и настройка

### 1️⃣ Клонирование репозитория

```sh
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
2️⃣ Создание виртуального окружения (рекомендуется)
sh
Копировать
Редактировать
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Установка зависимостей
sh
Копировать
Редактировать
pip install -r requirements.txt
4️⃣ Настройка settings.py
Откройте settings.py и добавьте параметры подключения к MongoDB:

python
Копировать
Редактировать
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mydatabase',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
        }
    }
}
5️⃣ Запуск миграций
sh
Копировать
Редактировать
python manage.py makemigrations
python manage.py migrate
6️⃣ Запуск сервера
sh
Копировать
Редактировать
python manage.py runserver
Сервер будет доступен по адресу http://127.0.0.1:8000/.

🛠 Технологии
Python 3.x
Django
HTML
CSS
```
