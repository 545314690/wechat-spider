# coding:utf-8
from sqlalchemy import text

from db.basic_db import db_session
from db.models import User
from decorators.decorator import db_commit_decorator


@db_commit_decorator
def save_users(users):
    db_session.add_all(users)
    db_session.commit()


@db_commit_decorator
def save(user):
    db_session.add(user)
    db_session.commit()


def get_by_id(id):
    return db_session.query(User).filter(User.id == id).first()


def get_by_alias(alias):
    return db_session.query(User).filter(User.alias == alias).first()


def get_user_by_nickname(nickname):
    return db_session.query(User).filter(User.nickname == nickname).first()


@db_commit_decorator
def set_crawled(id, result):
    """
    该表适用于用户抓取相关逻辑
    :param uid: 被抓取用户id
    :param result: 抓取结果
    :return: None
    """
    user = db_session.query(User).filter(User.id == id).first()
    if user:
        if user.is_crawled == 0:
            user.is_crawled = result
    else:
        user = User(id=id, is_crawled=result)
        db_session.add(user)
    db_session.commit()


@db_commit_decorator
def set_is_monitored(id, is_monitored):
    """
    :param id: 用户id
    :param is_monitored: 是否监控
    :return: None
    """
    user = get_by_id(id)
    if user is not None:
        user.is_monitored = is_monitored
        db_session.commit()

def get_is_monitored():
    """
    获取所有需要监控的用户
    :return:
    """
    return db_session.query(User).filter(text('is_monitored=1')).all()

@db_commit_decorator
def set_enable(id, enable):
    """
    :param id: 用户id
    :param is_monitored: 是否监控
    :return: None
    """
    user = get_by_id(id)
    if user is not None:
        user.enable = enable
        db_session.commit()
