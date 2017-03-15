# 爬取三生三世的所有集数
import requests
import re


url = 'http://v.qq.com/detail/j/j6cgzhtkuonf6te.html'
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
file = open('find_href.txt', 'w')
req = requests.get(url, headers)
req.encoding = 'utf-8'
# 获得html文本
html = req.text
txt_pre = html.split('\n')
txt = ''
for i in txt_pre:
	txt =txt + i.strip('\n')
find_div = re.findall(r'<div.+?</div>', txt)
for i in find_div:
	find_a = re.findall(r'<a href=.+?<span itemprop=', i)
	for j in find_a:
		find_href = re.findall(r'href="(.+?)"', j)
		if find_href != []:
			for k in find_href:
				file.write(k + '\n')
