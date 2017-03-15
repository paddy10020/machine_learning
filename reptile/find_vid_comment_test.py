import urllib.request
import json
# 提取评论
url = r'https://coral.qq.com/article/1743283224/comment?commentid=0&reqnum=10'
headers = {
    "Host": "www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive"
}
# req = requests.get(url, stream=True)
# print(req.text)
html = urllib.request.urlopen(url)
a = html.read()
b = a.decode()
# print(b)
jscontent = json.loads(b)
# a = jscontent['data']
comments = jscontent['data']['commentid']
file = open('find_comment.txt', 'w')
for i in comments:
	file.write(i['content'] + '\n')

