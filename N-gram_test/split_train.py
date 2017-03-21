# coding:utf-8
import re

a = re.compile(r'^\d+\s([^\W,^\d].*?[^\d])[\s,_]')
file = open('train.conll', 'r', encoding='utf-8')
txt_per = file.readlines()
txt = list('str')
for i in txt_per:
	if not i == []:
		tmp = a.findall(i)
		if not tmp == []:
			txt.append(tmp.pop(0))

file.close()
file = open('train.txt', 'w', encoding='utf-8')
for i in txt:
	file.write(i + '\n')
file.close()


