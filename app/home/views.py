from flask import Blueprint, jsonify

from app.home.models import Area
from app.utils.json_utils import to_list

home = Blueprint('home', __name__)

# {
#     status:200
#     msg:
#     hots:[],
#     areas:{'A':[],'B':[]}
# }


'''

'''

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
