import json
import random
import re
import time

import requests
from spider import headers

from  spider.logs.logger import logger
gzlist = []
file_seeds = open('keyword.txt', 'r',encoding='utf-8')
for line in file_seeds:
    gzlist.append(line.replace("\n", ""))
logger.info(gzlist)
file_seeds.close()

url = 'https://mp.weixin.qq.com'
header = {
    "HOST": "mp.weixin.qq.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
}

with open('cookie.txt', 'r', encoding='utf-8') as f:
    cookie = f.read()
cookies = json.loads(cookie)
response = requests.get(url=url, cookies=cookies)
token = re.findall(r'token=(\d+)', str(response.url))[0]

def searchPage(kw, begin, count):
    logger.info('开始search关键词=========>：' + str(begin) + ':', kw)
    biz_file = open('biz/biz_' + kw + '.txt', 'a+', encoding='utf-8')
    biz_file_json = open('biz/biz_' + kw + '.json', 'a+', encoding='utf-8')
    query_id = {
        'action': 'search_biz',
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': query,
        'begin': '{}'.format(str(begin)),
        'count': '5',
    }
    search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
    search_response = requests.get(search_url, cookies=cookies, headers=header, params=query_id)
    lists = search_response.json().get('list')
    max_num = search_response.json().get('total')
    for item in lists:
        json_str = json.dumps(item,ensure_ascii=False)
        logger.info(json_str)
        biz_file.write(item.get('fakeid') + '\n')
        biz_file_json.write(json_str + '\n')
    num = int(int(max_num) / 5)
    begin = int(begin)
    while max_num > begin:
        time.sleep(10)
        # query_id['begin'] = '{}'.format(str(begin));
        logger.info('翻页###################begin=', begin)
        try:
            begin += 5
            searchPage(kw, begin, 5)
            num -= 1
        except:
            logger.error('采集异常！！！！！！！')
    biz_file.close()
    biz_file_json.close()
for query in gzlist:
    searchPage(query, 0, 5)
    logger.info('完成采集公众号=========>：', query)
