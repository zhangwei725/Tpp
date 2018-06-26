from flask import Blueprint, request, jsonify
from flask_mail import Message

from app.ext import db, mail
from app.user.models import User

user = Blueprint('user', __name__)


@user.route('/login/')
def login():
    pass


'''
username
password
email
is_active 1激活 0未激活 
'''


@user.route('/register/', methods=['POST', 'GET'])
def register():
    result = {}
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        email = request.values.get('email')
        if username and password and email:
            # User.query.withenties(User.username)
            user = User.query.filter(User.username == username or User.email == email).all()
            if user:
                result.update(msg='账号或者邮箱已经存在', status=-2)
            else:
                user = User(username=username, password=password, email=email)
                db.session.add(user)
                db.session.commit()
            #         发送激活的邮箱
            msg = Message("Hello",
                          sender="18614068889@163.com",
                          recipients=['36558563@qq.com'])
            mail.send(msg)
        else:
            result.update(msg='必要参数不能为空', status=-1)
    else:
        result.update(msg='错误的请求方式', status=400)
    return jsonify(result)


@user.route('/1/', methods=['POST', 'GET'])
def test_send():
    msg = Message("激活邮件",
                  body='用户您好!!',
                  html="<a href=''>激活</a>",
                  sender="18614068889@163.com",
                  recipients=['18614068889@163.com'])
    mail.send(msg)
    return '请激活'
