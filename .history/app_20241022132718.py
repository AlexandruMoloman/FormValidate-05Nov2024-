from flask import Flask, render_template, request, redirect, url_for, flash
import re
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)  # Добавлено поле Surname
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name} {self.surname}>'

@app.route('/')
def home():
    message = "Это сообщение из app.py"
    return render_template('home.html', message=message)

@app.route('/greet/<name>')
def greet_name(name):
    return render_template('greet.html', name=name)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    surname = request.form['surname']

    # Проверка имени
    if not name or not re.match("^[A-Za-z]+$", name):
        flash("Пожалуйста, введите корректное имя (только буквы).")
        return redirect(url_for('home'))

    # Проверка фамилии
    if not surname or not re.match("^[A-Za-z]+$", surname):
        flash("Фамилия должна содержать только буквы.")
        return redirect(url_for('home'))

    # Сохранение в базу данных
    new_user = User(name=name, surname=surname, password="default")  # Добавлено значение по умолчанию для пароля
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('greet_name', name=name))

# Создание базы данных
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
