from flask import Flask, render_template,request,redirect,url_for,flash
import re

app.config['SQLALHEMY_']

app=Flask(__name__)
app.secret_key='supersecretkey'


# First Route
@app.route('/')
def home():
    message="This Text From app.py"
    return render_template('home.html', message=message)

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

    return render_template('greet.html', name=name)


    

if __name__== '__main__':
    app.run(debug=True, host=127.0.0.1, port=8080)