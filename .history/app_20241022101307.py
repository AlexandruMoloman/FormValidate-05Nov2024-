from flask import Flask, render_template,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)