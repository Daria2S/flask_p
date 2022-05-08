from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello from Daria"

@app.route('/daria')
def daria():
    return "I am programmer "

if __name__=='_main_':
    app.run(debug=True)
    