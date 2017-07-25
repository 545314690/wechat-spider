# -*-coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean, INTEGER, DateTime

from db.basic_db import Base, engine
from db.tables import *


class LoginInfo(Base):
    # 登录账号表 login_info
    __tablename__ = 'login_info'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(50), nullable=False)
    status = Column(INTEGER)
    enable = Column(Boolean, default=1, server_default='1')


class User(Base):
    # 用户表 wechat_user
    __tablename__ = 'wechat_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(100), default='', server_default='')
    alias = Column(String(100), default='', server_default='')
    service_type = Column("service_type", INTEGER, default=1, server_default='1')
    fakeid = Column("fakeid", String(100), default='', server_default='')
    description = Column("description", String(500), default='', server_default='')
    round_head_img = Column("round_head_img", String(500), default='', server_default='')
    is_crawled = Column("is_crawled", INTEGER, default=0, server_default='0')
    is_monitored = Column("is_monitored", INTEGER, default=0, server_default='0')
    enable = Column("enable", INTEGER, default=1, server_default='1')
    # 这里需要设置默认值，否则空的话可能会存储None，可能会引发未catch的异常


class KeyWords(Base):
    # 关键词搜索表 keywords
    __tablename__ = 'keywords'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    keyword = Column("keyword", String(200), unique=True)
    enable = Column("enable", INTEGER, default=1, server_default='1')


class WeChatData(Base):
    # 微博信息表 weibo_data
    __tablename__ = 'wechat_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column("title", String(100), default='', server_default='')
    content = Column("content", String(6000), default='', server_default='')
    like_num = Column("like_num", INTEGER, default=0, server_default='0')
    read_num = Column("read_num", INTEGER, default=0, server_default='0')
    uname = Column("uname", String(20))
    url = Column("url", String(300))
    head_img = Column("head_img", String(500), default='', server_default='')
    pub_time = Column("pub_time", DateTime)

Base.metadata.create_all(engine)#创建表
#Base.metadata.drop_all(engine)   #删除表
