# SELECT * FROM area where  parent_id = 0
import datetime

from app.ext import db


class Area(db.Model):
    area_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    parent_id = db.Column(db.Integer, index=True)
    pingyin = db.Column(db.String(100), nullable=False, index=True)
    key = db.Column(db.String(10))
    is_hot = db.Column(db.Boolean, default=False)


# 电影
class Movie(db.Model):
    __tablename__ = 'movies'
    mid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    showname = db.Column(db.String(64), unique=True, nullable=False, index=True)
    shownameen = db.Column(db.String(64), nullable=False, index=True)
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(64))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    screeningmodel = db.Column(db.String(10))
    openday = db.Column(db.DateTime, default=datetime.datetime.now())
    backgroundpicture = db.Column(db.String(64))
    flag = db.Column(db.Boolean, default=True)
    isdelete = db.Column(db.Boolean, default=False)
    # hs = db.relationship('HallSchedule', back_populates='hs')
