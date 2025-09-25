from flask import Flask 
from flask import render_template
import sqlite3
from flask import request

app = Flask(__name__)

connection = sqlite3.connect('my_database.db' , check_same_thread=False)
cursor = connection.cursor() 

def productDB(): 
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

def one_productDB(id): 
    listDB = cursor.execute('SELECT * FROM product WHERE id='+id)
    return listDB.fetchall()

@app.route('/') #главная страница
def index ():
    shop= productDB()
    return render_template("index.html", shop = shop)

@app.route('/about') #о нас
def about():
    return render_template("about.html")

@app.route('/catalog') #каталог
def catalog ():
    return render_template("catalog.html")

@app.route('/account') #аккаунт
def account ():
    return render_template("account.html")

@app.route('/contact') #контакты 
def contact():
    return render_template("contact.html")

@app.route('/user/<username>')
def user_profile(username):
    return render_template("index.html", name = username)

@app.route("/login")
def login():
    return render_template("login.html", title="Вход и регистрация")

@app.route('/zaiavka/<id>') # Обработчик заявки
def zaiavka(id):
    tovar = one_productDB(id)
    return render_template ('zaiavka.html',tovar= tovar)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # Полный список товаров с изображениями
    all_products = [
        
        {
            "name": "кофта Snug", 
            "price": "2500.0",
            "image": "https://avatars.mds.yandex.net/i?id=f9e3115be79672a9e69fd3757d9f231db7a48895-4532150-images-thumbs&n=13"  
        },
        {
            "name": "футболка Comfy", 
            "price": "2500.0",
            "image": "https://avatars.mds.yandex.net/i?id=941517b6b6606f9b99bbc2a9d958f07089416083-5452154-images-thumbs&n=13"
        },
        {
            "name": "куртка Staple", 
            "price": "5000.0",
            "image": "https://avatars.mds.yandex.net/i?id=8e5fd2f2f0d5a3aadc18448b19ac4953ab7ce740-3892269-images-thumbs&n=13"
        },
        {
            "name": "бомбер Edge", 
            "price": "4500.0",
            "image": "https://avatars.mds.yandex.net/i?id=60a40efdffda2fdaedfd16d10e9054607a1034c6-12716919-images-thumbs&n=13"
        },
        {
            "name": "шорты Zen", 
            "price": "3500.0",
            "image": "https://avatars.mds.yandex.net/i?id=4d6a1bc93a9b192ecf78acd0e76eb313297921a6-17016445-images-thumbs&n=13"
        },
        {
            "name": "джинсы Softie", 
            "price": "5000.0",
            "image": "https://avatars.mds.yandex.net/i?id=10f47412799b24e8e334e034e8d17ff8290b4c1a-4289847-images-thumbs&n=13"
        },
        {
            "name": "трико Nimbus", 
            "price": "4000.0",
            "image": "https://avatars.mds.yandex.net/i?id=06f5ecbb8fd9804992c5f22e9f3ed9adc744193f-5221595-images-thumbs&n=13"
        },
        {
            "name": "брюки Hush", 
            "price": "5500.0",
            "image": "https://avatars.mds.yandex.net/i?id=b9fb01f295293abc17b5f7c5cb44bc1d5e99a41e6e21a42f-10267148-images-thumbs&n=13"
        },
        {
            "name": "кеды Urban", 
            "price": "3500.0",
            "image": "https://avatars.mds.yandex.net/i?id=ce0eb70ed4ac02c06a78f69be52220b82bca3e7c-5151471-images-thumbs&n=13"
        },
        {
            "name": "кроссовки Daily", 
            "price": "5000.0",
            "image": "https://avatars.mds.yandex.net/i?id=4e2a2ca7ed8147b946b958f06dbc4bca7f73fb28-5147200-images-thumbs&n=13"
        },
        {
            "name": "ботинки Canvas", 
            "price": "4500.0",
            "image": "https://avatars.mds.yandex.net/i?id=7e203bdf03c006b77844d0c70a4725215a39b00a-5433932-images-thumbs&n=13"
        },
        {
            "name": "шлепки Zest", 
            "price": "4000.0",
            "image": "https://cdn1.ozone.ru/s3/multimedia-d/6711432205.jpg"
        }
    ]

    # Фильтрация товаров по запросу
    if query:
        filtered_products = [product for product in all_products 
                           if query.lower() in product['name'].lower()]
    else:
        filtered_products = []
    
    return render_template('search.html', 
                         query=query, 
                         products=filtered_products)



if __name__ == '__main__':  #точка входа нашей программы
    print("сервер запущен") #для проверки
    app.run (debug=True)
 