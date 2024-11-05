from flask import Flask, render_template, request, redirect, url_for,flash
import re
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key='supersecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    

@app.route('/')
def home():
    message = "This message is from app.py"
    return render_template('home.html', message=message)

@app.route('/greet/<name>')
def greet_name(name):
    return render_template('greet.html', name=name)

@app.route ('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    password = request.form['password']

    if not name or not re.match("^[A-Za-z]+$", name):
        flash("Please enter valide Name! (letters only).")
        return redirect(url_for('home'))


    if not password or not re.match("^[A-Za-z]+$", password):
        flash("Password should content minimum one symbol and Upper Letter")
        return redirect(url_for('home'))

    return redirect(url_for('greet_name', name=name,  password=password))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)