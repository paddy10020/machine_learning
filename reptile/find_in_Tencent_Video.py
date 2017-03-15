import requests
import re
import urllib.request
import json


# 从给出的url中找到评论信息
class FUC:
	def __init__(self):
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		self.comment_num = 20

	def changeCommentNum(self, num):
		self.comment_num = num

	def FindUrlList(self,Url):
		self.url_list_target = Url
		self.url_list = []
		tmp = requests.get(self.url_list_target, self.headers).text
		txt_pre = tmp.split('\n')
		txt = ''
		for i in txt_pre:
			txt = txt + i.strip('\n')
		find_div = re.findall(r'<div.+?</div>', txt)
		for i in find_div:
			find_a = re.findall(r'<a href=.+?<span itemprop=', i)
			for j in find_a:
				find_href = re.findall(r'href="(.+?)"', j)
				if find_href != []:
					for k in find_href:
						self.url_list.append(k)
		return self.url_list

	# 找到targetid
	def FindTargetId(self):
		self.vid = re.split(r'[/,.]', self.url).pop(8)
		self.targetid_url = 'http://ncgi.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid=' + self.vid
		self.req = requests.get(self.targetid_url, self.headers)
		self.req.encoding = 'utf-8'
		self.find_id = re.findall(r'"comment_id":"(\d+?)"', self.req.text)
		self.targetid = self.find_id.pop(0)

    # 找到评论
	def FindComment(self,):
		self.comment_url = r'https://coral.qq.com/article/' + self.targetid + '/comment?commentid=0&reqnum=' + str(self.comment_num)
		self.js_txt = urllib.request.urlopen(self.comment_url).read().decode()
		self.js = json.loads(self.js_txt)
		self.comments = self.js['data']['commentid']
		for i in self.comments:
			print(i['content'])

	def find(self, URL):
		self.url = URL
		self.FindTargetId()
		self.FindComment()

	def findListUrl(self, urlList):
		for self.url in urlList:
			self.FindTargetId()
			self.FindComment()


file = open('find_href.txt', 'r')
a = FUC()
# a.find('http://v.qq.com/x/cover/j6cgzhtkuonf6te/d0022fbmgl2.html')
# a.findListUrl(file.readlines())
a.findListUrl(a.FindUrlList('http://v.qq.com/detail/j/j6cgzhtkuonf6te.html'))
