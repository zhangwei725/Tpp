from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def init_ext(app):
    init_db(app)
    init_mail(app)


# 配置数据库orm框架
db = SQLAlchemy()
# 数据库迁移
migrate = Migrate()


# 初始化数据库配置
def init_db(app):
    db.init_app(app=app)
    migrate.init_app(app, db)


# 邮箱的配置
mail = Mail()


def init_mail(app):
    mail.init_app(app)
