from db import user
from db.login_info import get_by_id
from db.models import LoginInfo

from db.user import save
from util import json

save(LoginInfo(username='c',password='d',enable=0))

rts = json.dumps(get_by_id(1))  # 加上ensure_ascii=False 是解决中文乱码问题
print(rts)
rts = json.dumps(user.get_by_id(1))
print(rts)
