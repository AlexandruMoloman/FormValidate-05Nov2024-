# Третий маршрут (приветствие с именем и фамилией)
@app.route('/greet/<name>/<surname>')
def greet_name(name, surname):
    return render_template('greet.html', name=name, surname=surname)

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

    # Перенаправление на страницу приветствия с именем и фамилией
    return redirect(url_for('greet_name', name=name, surname=surname))
