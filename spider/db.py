from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, DateTime, Boolean
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://anjian:topcom123@115.28.72.158:3306/wechat?charset=utf8", max_overflow=5,
                       encoding='utf-8')

Base = declarative_base()


# 创建单表
class Users(Base):
    __tablename__ = 'wx_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(150), index=True, nullable=False, unique=True)
    fakeid = Column(String(16))
    alias = Column(String(32), index=True, nullable=False, unique=True)
    round_head_img = Column(String(255))
    service_type = Column(Integer)
    history_gatherd = Column(Boolean, default=False)
    minit_home = Column(Boolean, default=False)
    enable = Column(Boolean, default=True)

    __table_args__ = (
        UniqueConstraint('id', name='id'),
        UniqueConstraint('nickname', name='nickname'),
        UniqueConstraint('alias', name='alias'),
    )


# 微信
class WeChat(Base):
    __tablename__ = 'wechat_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(String(1000))
    pubTime = Column(DateTime)


# 登录用户
class LoginUser(Base):
    __tablename__ = 'login_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(50), nullable=False)
    status = Column(Integer)
    enable = Column(Boolean, default=True)


Base.metadata.create_all(engine)  # 创建表
# Base.metadata.drop_all(engine)   #删除表
