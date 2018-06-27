from app.ext import db


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    # 表示False 未激活  True表示激活
    is_active = db.Column(db.Boolean, default=False)
