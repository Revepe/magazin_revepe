Revepe - Интернет-магазин одежды

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)

**Revepe** - интернет-магазин одежды на Flask с полным циклом онлайн-продаж. Проект включает каталог товаров, поиск товаров, вход в аккаунт и систему оформления заказов.

---

Быстрый старт

Предварительные требования

- Python 3.8 или выше
- Установленный pip

### Установка и запуск

1. **Клонируйте репозиторий**
bash
git clone [https://github.com/Revepe/magazin_revepe/tree/main/Project_revepe.git]
cd Project_revepe

1. Создайте и активируйте виртуальное окружение

bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

1. Установите зависимости

bash
pip install -r requirements.txt

1. Запустите приложение

bash
python app.py

Приложение будет доступно по адресу: http://127.0.0.1:5000

---

 Функциональность

 Покупательская зона

· Главная - каталог с карточками товаров
· О нас - информация как и почему был создан сайт
· Контакты - контактные данные
· Поиск - поиск товаров по названию
· Вход/регистрация - вход или регистрация
· Заявка - оформление заказа

 Технические особенности

· Сессии Flask для оформления заказов
· Адаптивный дизайн (ПК + мобильные устройства)
· SQLite база данных с резервным копированием
· Подготовка к HTTPS/SSL

---

 Структура проекта

project_revepe/
├── app.py                 # Основное приложение Flask
├── my_database.db         # База данных SQLite (создается автоматически)
├── proba.py               # проба
├── README.md              # вы находитесь здесь
│
├── static/                                      # Статические файлы
│   ├── photo_5377682891980534330_x.png          # лого сайта
│   └── style.css                                # базовый ксс файл для стиля всех страничек
│
└── templates/                  # HTML шаблоны
    ├── about.html              # Страница "О нас"
    ├── base.html               # Главная 
    ├── contact.html            # Контакты
    ├── index.html              # Главная
    ├── login.html              # Вход/Регистрация
    ├── Product.html            # карточка товара
    ├── search.html             # поиск
    ├── shop.html               # страничка магазина товаров
    └── zaiavka.html            # Заявка

 
---

Технологический стек

Бэкенд:

· Python 3.8+
· Flask 2.0+
· Flask-Session
· SQLite3

Фронтенд:

· HTML CSS
· Jinja2 шаблоны

База данных:

· SQLite с моделями:
  · Товары (название, описание, цена, бренд, изображение)

---

Развертывание

Локальная разработка

bash
python app.py
`

Продакшен (рекомендации)

· Используйте WSGI сервер (Gunicorn)
· Настройте Nginx как reverse proxy
· Включите HTTPS с SSL сертификатом
· Регулярное резервное копирование database.db

---

Участие в разработке

Приветствуются contributions! Порядок действий:
1. Форкните репозиторий
2. Создайте feature branch (git checkout -b feature/AmazingFeature)
3. Зафиксируйте изменения (git commit -m 'Add AmazingFeature')
4. Запушьте ветку (git push origin feature/AmazingFeature)
5. Откройте Pull Request

---

Лицензия

Распространяется под лицензией MIT. См. файл LICENSE для деталей.

---
