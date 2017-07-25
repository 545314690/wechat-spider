# -*-coding:utf-8 -*-

from db.basic_db import metadata, Base, engine

Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)   #删除表
