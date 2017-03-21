# coding:utf-8
# 统计两个字符一起出现的概率

import json
file = open('train_count.txt', 'r', encoding='utf-8')
txt_list = file.readlines()
file.close()
char_list_dict = list()
for i in txt_list:
    tmp = dict()
    tmp = json.loads(i.strip('\n'))
    char_list_dict.append(tmp)

test_txt = '大强'
tmp1 = test_txt[0]
tmp2 = test_txt[1]
tmp1_dict = dict()
tmp2_dict = dict()
for i in char_list_dict:
    if i['char'] == tmp1:
        tmp1_dict = i
    if i['char'] == tmp2:
        tmp2_dict = i
print(tmp1_dict)
print(tmp2_dict)

rate1 = tmp1_dict['count']/len(char_list_dict)
if tmp1 in tmp2_dict.keys():
    rate2 = tmp2_dict[tmp1] / tmp2_dict['count']
    print(rate1*rate2)
else:
    print(0)
