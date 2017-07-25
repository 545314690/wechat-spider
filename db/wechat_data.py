# coding:utf-8
from sqlalchemy import text
from db.basic_db import db_session
from db.models import WeChatData
from decorators.decorator import db_commit_decorator


@db_commit_decorator
def insert(wechat_data):
    # 存入数据的时候从更高一层判断是否会重复，不在该层做判断
    db_session.add(wechat_data)
    db_session.commit()


def get_by_url(url):
    """
    :param url: url
    :return: 
    """
    return db_session.query(WeChatData).filter(WeChatData.url == url).first()


@db_commit_decorator
def insert_wechat_datas(wechat_datas):
    for data in wechat_datas:
        r = get_by_url(data.url)
        if not r:
            db_session.add(data)
    db_session.commit()