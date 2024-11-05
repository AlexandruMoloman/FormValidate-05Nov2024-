from flask import Flask, render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import re





app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key='supersecretkey'


# First Route
@app.route('/')
def home():
    message="This Text From app.py"
    return render_template('home.html', message=message)

#Third Route ('/greet/<name>')
@app.route('/greet/<name>')
def greet_name(name):
    return render_template('greet.html', name=name)

#Second Route
@app.route('greet', methods=['POST'])
def greet():
    name=request.form['name']
    surname=request.form['surname']

#Check validations Name
    if name or not re.match('^[A-Zaa-z]+$', name):
        flash("Name is not Valid (Leters Only)")
        return redirect(url_for('home'))

#Check validations SurName
    if surname or re.match('^[A-Za-z]+$', surname):
        flash("Surname is not valid (Letters Only)")
        return redirect(url_for('home'))

        #Add user in db
        new_user = User(name=name, surname=surname)
        db.session.add(new_user)
        db.session.commit()

    return render_template('greet_name', name=name)

    with app.app_context():
        db.create_all()
    

if __name__== '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)