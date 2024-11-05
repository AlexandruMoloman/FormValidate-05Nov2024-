from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'supersecretkey'


# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'


# Первый маршрут (главная страница)
@app.route('/')
def home():
    message = "This Text From app.py"
    return render_template('home.html', message=message)


# Третий маршрут (приветствие с именем)
@app.route('/greet/<name>')
def greet_name(name):
    return render_template('greet.html', name=name)


# Второй маршрут (обработка формы)
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    surname = request.form['surname']

    # Валидация имени
    if not name or not re.match("^[A-Za-z]+$", name):
        flash("Name is not valid (letters only).")
        return redirect(url_for('home'))

    # Валидация фамилии
    if not surname or not re.match("^[A-Za-z]+$", surname):
        flash("Surname is not valid (letters only).")
        return redirect(url_for('home'))

    # Добавление пользователя в базу данных
    new_user = User(name=name, surname=surname)
    db.session.add(new_user)
    db.session.commit()

    # Перенаправление на страницу приветствия
    return redirect(url_for('greet_name', name=name))


# Создание базы данных
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
