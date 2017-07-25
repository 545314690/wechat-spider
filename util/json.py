import json

from util.alchemy_encoder import AlchemyEncoder


def dumps(object):
    return json.dumps(object, cls=AlchemyEncoder, ensure_ascii=False)  # 加上ensure_ascii=False 是解决中文乱码问题
