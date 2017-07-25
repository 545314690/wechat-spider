# -*-coding:utf-8 -*-
from sqlalchemy import Table, Column, INTEGER, String, DateTime
from db.basic_db import metadata

# 登陆帐号表 login_info
login_info = Table("login_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("username", String(100), unique=True),
                   Column("password", String(200)),
                   Column("enable", INTEGER, default=1, server_default='1'),
                   )
# 用户表 wxuser
wechat_user = Table("wechat_user", metadata,
                    # 这里需要设置默认值，否则空的话可能会存储None，可能会引发未catch的异常
                    Column("id", INTEGER, primary_key=True, autoincrement=True),
                    Column("nickname", String(100), default='', server_default=''),
                    Column("alias", String(100), default='', server_default=''),
                    Column("service_type", INTEGER, default=1, server_default='1'),
                    Column("fakeid", String(100), default='', server_default=''),
                    Column("description", String(500), default='', server_default=''),
                    Column("round_head_img", String(500), default='', server_default=''),
                    Column("is_crawled", INTEGER, default=0, server_default='0'),
                    Column("is_monitored", INTEGER, default=0, server_default='0'),
                    Column("enable", INTEGER, default=1, server_default='1')
                    )
# 关键词搜索表 keywords
keywords = Table('keywords', metadata,
                 Column("id", INTEGER, primary_key=True, autoincrement=True),
                 Column("keyword", String(200), unique=True),
                 Column("enable", INTEGER, default=1, server_default='1'),
                 )

# 微博信息表 weibo_data
wechat_data = Table('wechat_data', metadata,
                    Column("id", INTEGER, primary_key=True, autoincrement=True),
                    Column("title", String(100), default='', server_default=''),
                    Column("content", String(6000), default='', server_default=''),
                    Column("like_num", INTEGER, default=0, server_default='0'),
                    Column("read_num", INTEGER, default=0, server_default='0'),
                    Column("uname", String(20)),
                    Column("url", String(300)),
                    Column("head_img", String(500), default='', server_default=''),
                    Column("publish_time", DateTime),
                    )

__all__ = ['login_info', 'wechat_user', 'keywords', 'wechat_data']
