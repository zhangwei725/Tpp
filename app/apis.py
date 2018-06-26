from flask import Blueprint

# 蓝图注册
from app.user.views import user


def register_blue(app):
    app.register_blueprint(user, url_prefix='/user')
