from flask import Blueprint, request, jsonify

from app.cinema.models import Cinema
from app.cinema.schema import cinemas_schema
from app.utils.json_utils import to_list

cinema_blue = Blueprint('cinema_blue', __name__)


@cinema_blue.route('/list/')
def cinemas():
    result = {}
    try:
        # 参数部分
        page = request.values.get('page', default=1, type=int)
        size = request.values.get('size', default=10, type=int)
        # sort 1 按评分降序   2 表示 按评分升序 0表示综合排序
        sort = request.values.get('sort', default=0, type=int)
        # 城市的区县
        dist = request.values.get('dist')
        # 城市
        city = request.values.get('city')
        # 搜索电影院的名称
        keyword = request.values.get('keyword')
        if city:
            # 根据城市分页加载数据
            # 返回一个新的query对象
            query = Cinema.query.filter(Cinema.city == city)
            # cinemas = Cinema.query.filter(Cinema.city == city).all()
            # to_list(cinemas)
            #    选择了区县
            if dist:
                query = query.filter(Cinema.district == dist)
            #  影院名称搜索
            if keyword:
                query = query.filter(Cinema.name.like('%' + keyword + '%'))
            if sort:
                # 升序
                if sort == 1:
                    query = query.order_by(Cinema.score.desc())
                else:
                    #  降序
                    query = query.order_by(Cinema.score)
            paginate = query.paginate(page=page, per_page=size, error_out=False)
            result.update(status=200, msg='success', cinemas=to_list(paginate.items))
        else:
            result.update(status=-1, msg='no param city')
    except Exception as e:
        result.update(status=404, msg='fail')
    return jsonify(result)
