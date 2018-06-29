from flask import Blueprint, jsonify
from sqlalchemy import func

from app.home.models import Area, Movie
from app.utils.json_utils import to_list

home = Blueprint('home', __name__)

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


@home.route('/areas/')
def get_ares():
    result = {}
    # with_entities 过滤列
    # 相当于 db.session
    ares = {}
    try:
        for key in keys:
            # ares[key] = Area.query.with_entities(Area.name, Area.area_id).filter(Area.key == key).all()
            area_list = Area.query.filter(Area.key == key).all()
            if area_list:
                ares[key] = to_list(area_list)
        result.update(msg='success', status=200, ares=ares)
    except Exception as e:
        result.update(msg='查询失败', status=404)
    return jsonify(result)


# SELECT  COUNT(*) FROM MOVIE GROUP BY FLAG
@home.route('/moves/', methods=['GET', 'POST'])
def movies():
    result = {}
    try:
        movie = {}
        # 分组查出热门影片和热映的影片数量
        counts = Movie.query.with_entities(Movie.flag, func.count('*')).group_by(Movie.flag).all()
        # cursor = Movie.query.execute('SELECT COUNT(*) FROM movies GROUP BY flag')
        #
        # 查热门影片的前5部
        hot_movies = Movie.query.filter(Movie.flag == 1).limit(5).all()
        # 查询即将上映的前5部
        show_movies = Movie.query.filter(Movie.flag == 2).limit(5).all()
        movie.update(counts=counts, hot_movies=to_list(hot_movies), show_movies=to_list(show_movies))
        result.update(status=200, msg='success', data=movie)
    except Exception as e:
        result.update(status=404, msg='fail')
    return jsonify(result)
