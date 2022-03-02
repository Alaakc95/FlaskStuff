from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello, world!'

@app.route('/index')
def indexpage():
    return 'This is the index page :)'

if __name__ == '__main__':
    app.run()