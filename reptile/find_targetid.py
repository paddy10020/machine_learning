# coding:utf-8
import requests
import re
# 查找targetid
url = 'http://ncgi.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid=d0022fbmgl2'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

req = requests.get(url, headers)
req.encoding = 'utf-8'
# print(req.text)
find_id = re.findall(r'"comment_id":"(\d+?)"', req.text)
targetid = find_id.pop(0)
print(targetid)
targetid.split

