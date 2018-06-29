from flask import Blueprint, request, jsonify

from app.home.models import Movie
from app.movies.schema import movies_schema

movies_blue = Blueprint('movies', __name__)

"""
参数flag
参数page
参数size

"""


# movie/list/?flag=1
@movies_blue.route('/list/')
def movie():
    result = {}
    try:
        # 判断是热门还是即将上映参数
        flag = request.values.get('flag', default=1, type=int)
        #  分页参数
        page = request.values.get('page', default=1, type=int)
        size = request.values.get('size', default=10, type=int)
        # 分页查询数据
        paginate = Movie.query.filter(Movie.flag == flag).paginate(page=page, per_page=size, error_out=False)
        """
        total 总条数
        pages 总页数
        items 数据
        """
        # 封装前端界面需要的数据
        pagination = {'total': paginate.total, 'pages': paginate.pages}
        # 要显示的主要数据
        movies = movies_schema.dump(paginate.items)
        # 组装返回的数据
        result.update(status=200, msg='success', data=movies.data, paginate=pagination)
    except:
        result.update(status=404, msg='fail')
    return jsonify(result)
