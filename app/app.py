from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_apscheduler import APScheduler


from app.services.wx import WxServer

app = Flask(__name__)
app.config.from_object('app.configs.config.Wx')


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/success')
def success_page():
    return render_template('success.html')


@app.route('/failed')
def failed_page():
    return render_template('failed.html')


@app.route('/login', methods=['post'])
def login():
    user_list = WxServer().get_wx_user()
    username = request.form['username']
    password = request.form['password']
    # 登录逻辑判断
    if login_service(username, password):
        return redirect(url_for('success_page'))
    else:
        return redirect(url_for('failed_page'))


def login_service(username, password):
    """
    登录逻辑判断
    :param username:
    :param password:
    :return:
    """
    if 'admin' == username and '123456' == password:
        return True
    else:
        return False


@app.before_first_request
def first_request():
    """
    系统初始化启动
    """
    print('first_request')
    scheduler = APScheduler()
    scheduler.add_job(func=WxServer().sync_user, id='1', trigger='interval', seconds=1, replace_existing=True)
    scheduler.start()
