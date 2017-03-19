# coding:utf-8
import re

file = open('data.txt', 'r', encoding='utf-8')
origin = file.readlines()
file.close()
a_pre = re.compile(r'^\d+\s(.*?)[,,\s,_]')
txt_list = []
for i in origin:
	a = a_pre.findall(i)
	if not a == []:
		txt_list.append(a.pop(0))


def split_chinese(txt, dict_data, result):
	if len(txt) >= 3:
		if txt[0:3] in dict_data:
			result.append(txt[0:3])
			txt = txt[3:len(txt)]
			split_chinese(txt, dict_data, result)
		elif txt[0:2] in dict_data:
			result.append(txt[0:2])
			txt = txt[2:len(txt)]
			split_chinese(txt, dict_data, result)
		else:
			result.append(txt[0])
			txt = txt[1:len(txt)]
			split_chinese(txt, dict_data, result)

	elif len(txt) == 2:
		if txt[0:2] in dict_data:
			result.append(txt[0:2])
		else:
			result.append(txt[0:1])
			result.append(txt[1:2])

a = '我是中国人，但我不是好人'
a_list = re.split(r'[,.，。]', a)
test_list = []
for i in a_list:
	split_chinese(i, txt_list, test_list)
print('-'*10)
print('原句:' + a)
print('-'*10)
print('分句:')
for i in test_list:
	print(i + ' ')
print('-'*10)
