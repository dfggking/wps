from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return 'Hello World! {}'.format(user_agent)


if __name__ == '__main__':
    app.run(debug=True)
