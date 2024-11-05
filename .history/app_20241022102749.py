from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    message = "This message is from app.py"
    return render_template('home.html', message=message)

@app.route ('/greet', method=['POST'])
def greet():
    name = request.form['name']
    password = request.form['password']
    return render_template('greet.html', name=name, password=password)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)