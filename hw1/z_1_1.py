""" Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна 
(шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

category = [
    {"title": 'Одежда', "func_name": 'dress'},
    {"title": 'Обувь', "func_name": 'shoes'},
    {"title": 'Игрушки', "func_name": 'toys'}
]

@app.route('/')
@app.route('/index/')
def index():
    return render_template('store_index.html', category=category)


@app.route('/info/')
def info():
    return render_template('store_info.html')


@app.route('/contacts/')
def contacts():
    return render_template('store_contacts.html')


@app.route('/dress/')
def dress():
    return render_template('store_dress.html')


@app.route('/shoes/')
def shoes():
    return render_template('store_shoes.html')


@app.route('/toys/')
def toys():
    return render_template('store_toys.html')


if __name__ == '__main__':
    app.run()
