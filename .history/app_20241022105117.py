from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    message = "Это сообщение из app.py"
    return render_template('home.html', message=message)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    password = request.form['password']

    # Проверка имени (только буквы)
    if not name or not re.match("^[A-Za-z]+$", name):
        flash("Пожалуйста, введите корректное имя (только буквы).")
        return redirect(url_for('home'))

    # Проверка пароля
    if not password or not re.match("^(?=.*[A-Z])(?=.*[!@#$%^&*(),.?\":{}|<>]).+$", password):
        flash("Пароль должен содержать минимум один символ и одну заглавную букву.")
        return redirect(url_for('home'))

    return redirect(url_for('greet_user', name=name))

@app.route('/greet_user/<name>')
def greet_user(name):
    return f'Привет, {name}! Ваш пароль был успешно проверен.'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
