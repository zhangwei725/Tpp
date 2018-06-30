import datetime

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
    # 屏幕的类型 1 表示普通的屏幕   2 3D  3 4D
    type = db.Column(db.Integer, default=1)
    # 是否删除
    is_delete = db.Column(db.Boolean, default=False)
    cinema = db.relationship('Cinema')


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
    #  电影的外键
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.mid'))
    # 影厅的外键
    hid = db.Column(db.Integer, db.ForeignKey('hall.hid'))
    #  影院id外键
    cid = db.Column(db.Integer, db.ForeignKey('cinemas.mid'))
    # 类名 查询
    # hall = db.relationship('Hall')
    # cinema = db.relationship('Cinema')
    # ???
    # movie = db.relationship('Movie')


# 座位表
class Seat(db.Model):
    __tablename__ = 'seat'
    seat_id = db.Column(db.Integer, primary_key=True)
    # 1 普通,2 沙发 3 豪华包间
    # type = db.Column(db.Integer, default=1)
    # 座位的x
    seat_x = db.Column(db.Integer)
    # 座位的y
    # 通过x y能确定一个座位
    seat_y = db.Column(db.Integer)
    # (1.表示可用,2表示损坏)
    status = db.Column(db.Integer, default=1)
    # 是否删除 1表示正常   0表示 记录被删除  表的公共字段
    is_delete = db.Column(db.Integer, default=1)
    # 该记录创建的时间  表的公共字段
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    # ====关联字段 =====
    # 影院的id
    cinema_id = db.Column(db.Integer, db.ForeignKey(Cinema.cid))
    # 影厅的id
    hall_id = db.Column(db.Integer, db.ForeignKey(Hall.hid))


class SeatSchedule(db.Model):
    ssid = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, db.ForeignKey(Seat.seat_id))
    # 影院的id
    cinema_id = db.Column(db.Integer, db.ForeignKey(Cinema.cid))
    # 影厅的id
    hall_id = db.Column(db.Integer, db.ForeignKey(Hall.hid))
    # 关联排档的id
    hsid = db.Column(db.Integer, db.ForeignKey(HallSchedule.hsid))
    # 1表示未锁定   2 表示锁定未支付   3表示锁定已支付
    status = db.Column(db.Integer, default=1)
    # 是否删除 1表示正常   0表示 记录被删除  表的公共字段
    is_delete = db.Column(db.Integer, default=1)
    # 该记录创建的时间  表的公共字段
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    seat = db.relationship('Seat')
