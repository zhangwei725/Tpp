# 洲   --> 国家 --- 省 --- 市 --- 区县 --->
# 湖北
# 武汉  黄石
# 武昌区

# SELECT * FROM area where  parent_id = 0
from app.ext import db


class Area(db.Model):
    area_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    parent_id = db.Column(db.Integer, index=True)
    pingyin = db.Column(db.String(100), nullable=False, index=True)
    key = db.Column(db.String(10))
    is_hot = db.Column(db.Boolean, default=False)
