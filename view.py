#view.py - контроллер
#----------- Django MVC -----------
#Model - db(База данных)
#View - controller(в нормальном MVC шаблоны, то что видит пользователь)
#Templates

from app import app
from flask import render_template

#декоратор можно и для разных путей тоже самое поведение
#@app.route('/')
#@app.route('/blog')
# def func():
#     ...какое-то поведение

@app.route('/')
def index():
    name = 'Dima Hinev'
    return render_template('index.html', name=name)

