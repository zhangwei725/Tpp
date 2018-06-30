from flask import Blueprint, request, jsonify

from app.cinema.models import Cinema, HallSchedule, Hall, SeatSchedule
from app.home.models import Movie
from app.utils.json_utils import to_dict

order = Blueprint('order', __name__)

# get获取
# post 提交
# put 修改数据
# delete 删除

# 选座
"""
必要参数:排片ID
必要参数 影片的id
必传参数 影院的id
"""


@order.route('/choose/')
def choose_seat():
    result = {}

    # 查询排片的数据
    hs = HallSchedule.query.get(1)
    # 查询影院的相关信息
    cinemas = Cinema.query.with_entities(Cinema.cid, Cinema.name).filter(Cinema.cid == 1).first()
    cinema = {}
    # 过滤字段转化成字段
    cinema.update(cid=cinemas[0], name=cinemas[1])

    # 查询影厅的相关的信息
    halls = Hall.query.with_entities(Hall.name).filter(Hall.hid == hs.hid).first()
    movies = Movie.query.with_entities(Movie.language, Movie.showname, Movie.screeningmodel, Movie.backgroundpicture) \
        .filter(Movie.mid == hs.movie_id).first()
    # 通过影院id 影厅的id 去查询相关的座位信息
    seat_list = SeatSchedule.query.filter(SeatSchedule.cinema_id == 1, SeatSchedule.hall_id == 1).all()
    # 第一个就是x y status
    result.update(status=200, msg='success', cinema=cinema, hall_schedule=to_dict(hs))

    return jsonify(result)

# order
