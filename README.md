AVELINE - Интернет-магазин одежды

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)

**AVELINE** - интернет-магазин одежды на Flask с полным циклом онлайн-продаж. Проект включает каталог товаров, корзину, избранное и систему оформления заказов.

---

Быстрый старт

Предварительные требования

- Python 3.8 или выше
- Установленный pip

### Установка и запуск

1. **Клонируйте репозиторий**
bash
git clone https://github.com/Sofia-claire/aveline.git
cd aveline

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

Приложение будет доступно по адресу: http://localhost:5000

---

 Функциональность

 Покупательская зона

· Главная страница - каталог товаров с карточками
· Коллекции брендов - фильтрация по брендам с баннерами
· Поиск товаров - поиск по названию и описанию
· Корзина покупок - добавление/удаление товаров, расчет суммы
· Избранное - сохранение товаров (иконка сердца)
· Оформление заказа - форма с контактными данными

 Технические особенности

· Сессии Flask для корзины и избранного
· Адаптивный дизайн (ПК + мобильные устройства)
· SQLite база данных с резервным копированием
· Подготовка к HTTPS/SSL

---

 Структура проекта

aveline/
├── app.py                 # Основное приложение Flask
├── database.db            # База данных SQLite (создается автоматически)
├── proba.py               # проба
├── README.md              # вы тут
│
├── static/               # Статические файлы
│   ├── banner1.jpg       #1 баннер
│   ├── banner2.jpg       #2 баннер
│   ├── background.png    #2 изображение для фона на всем сайте
│   ├── icons
│   │   └──brands-icon.png      # иконка брэнда
│   │   └──favorites-icon.png   # иконка избранного
│   │   └──history-icon.png     # иконка истории
│   │   └──instagram-icon.png   # иконка инсты
│   │   └──login-icon.png       # иконка логин
│   │   └──reviews-icon.png     # иконка оотзывов
│   │   └──telegram-icon.png    # иконка тг
│   └── product1.jpg            # фотокарточка 1 продукта
│   └── product2.jpg            # фотокарточка 2 продукта
│   └── product3.jpg            # фотокарточка 3 продукта
│   └── product4.jpg            # фотокарточка 4 продукта
│   └── product.css             # ксс файл для подробного стиля продукта
│   └── style.css               # базовый ксс файл для стиля всех страничек
│
└── templates/                  # HTML шаблоны
    ├── about.html              # Страница "О нас"
    ├── base.html               # Главная страница
    ├── brands_collection.html  # Корзина
    ├── brands.html             # Избранное
    ├── cart.html               # Корзина
    ├── checkout.html           # Страница "О нас"
    ├── favorites.html          # Избранное
    ├── index.html              # Главная страница
    ├── login.html              # вход/регистрация
    ├── menu.html               # Меню
    ├── order_success.html      # Заказ
    ├── page.html               # Коллекции брендов
    ├── proba.html              # пробный бд
    ├── produc.html             # карточка товара
    ├── search.html             # поиск
    └── shop.html               # страничка магазина товаров

 
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

Для добавления товаров используйте Flask shell или прямое редактирование базы данных. Пример добавления товара:

python
from app import app, db, Product

with app.app_context():
    new_product = Product(
        name="Платье летнее",
        description="Легкое летнее платье",
        price=2999,
        brand="Summer Collection",
        image="dress.jpg"
    )
    db.session.add(new_product)
    db.session.commit()

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
