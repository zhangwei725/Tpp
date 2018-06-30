from flask import Blueprint

# 蓝图注册

from app.cinema.views import cinema_blue
from app.home.views import home, movies
from app.movies.views import movie, movies_blue
from app.order.views import order
from app.user.views import user


def register_blue(app):
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(movies_blue, url_prefix='/movie')
    app.register_blueprint(cinema_blue, url_prefix='/cinema')
    app.register_blueprint(order, url_prefix='/order')
