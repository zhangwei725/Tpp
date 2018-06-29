from app.ext import db


# 影院
class Cinema(db.Model):
    __tablename__ = 'cinemas'
    cid = db.Column('mid', db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    city = db.Column(db.String(10))
    district = db.Column(db.String(10))
    address = db.Column(db.String(64))
    phone = db.Column(db.String(20))
    score = db.Column(db.Float(3, 1), default=10.0)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Float(3, 1), default=1.2)
    astrict = db.Column(db.Integer)
    flag = db.Column(db.Boolean, default=True)
    isdelete = db.Column(db.Boolean, default=False)

# 影厅
class Hall(db.Model):
    hid = db.Column(db.Integer, primary_key=True)
    # 影院的外键
    mid = db.Column(db.Integer, db.ForeignKey('cinemas.mid'))
    # 影院的名称
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    # 座位数
    seats = db.Column(db.Integer, default=0)
    # 是否删除
    is_delete = db.Column(db.Boolean, default=False)


# id
# 电影id
# 影厅id
# 原价
# 售价
# 放映时间
# 状态
# 1000 0000 00
# 影厅电影排期
class HallSchedule(db.Model):
    hsid = db.Column(db.Integer, primary_key=True)
    # 原价
    original_price = db.Column(db.Numeric(10, 2))
    # 折扣价
    dis_price = db.Column(db.Numeric(10, 2))
    # 开始放映的时间
    start_time = db.Column(db.DateTime)
    # 1未开始放映   2正在放映
    status = db.Column(db.Integer, default=1)
    is_delete = db.Column(db.Boolean, default=False)
    #   电影的外键
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.mid'))
    # 影厅的外键
    hid = db.Column(db.Integer, db.ForeignKey('hall.hid'))
    #  影院id外键
    cid = db.Column(db.Integer, db.ForeignKey('cinemas.mid'))
