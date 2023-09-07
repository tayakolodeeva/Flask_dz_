"""
Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя, 
а также будет произведено перенаправление на страницу приветствия, 
где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», 
при нажатии на которую будет удалён cookie-файл с данными пользователя и произведено 
перенаправление на страницу ввода имени и электронной почты.
"""
from flask import Flask, render_template, redirect, request, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return render_template('index.html', username=username)
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username') or 'Незнакомец'
        email = request.form.get('email')
        response = make_response(redirect(url_for('index')))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response
    return render_template('login.html', title='Вход')


@app.get('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)