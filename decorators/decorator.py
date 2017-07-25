# -*-coding:utf-8 -*-
from functools import wraps
from traceback import format_tb
from db.basic_db import db_session
from loggers.log import parser, crawler, storage


# 用于超时设置
def timeout_decorator(func):
    @wraps(func)
    def time_limit(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            crawler.error('抓取{url}失败，具体错误信息为{e},堆栈为{stack}'.format(url=args[0], e=e,
                                                                   stack=format_tb(e.__traceback__)[0]))
            return ''

    return time_limit


def db_commit_decorator(func):
    @wraps(func)
    def session_commit(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            storage.error('数据库操作失败，具体信息是{}'.format(e))
            db_session.rollback()
    return session_commit


def parse_decorator(return_type):
    """
    :param return_type: 用于捕捉页面解析的异常, 0表示返回数字0, 1表示返回空字符串, 2表示返回[],3表示返回False, 4表示返回{}, 5返回None
    :return: 0,'',[],False,{},None
    """
    def page_parse(func):
        @wraps(func)
        def handle_error(*keys):
            try:
                return func(*keys)
            except Exception as e:
                parser.error(e)

                if return_type == 5:
                    return None
                elif return_type == 4:
                    return {}
                elif return_type == 3:
                    return False
                elif return_type == 2:
                    return []
                elif return_type == 1:
                    return ''
                else:
                    return 0

        return handle_error

    return page_parse

