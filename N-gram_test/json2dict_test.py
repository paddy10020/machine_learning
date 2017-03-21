# coding:utf-8
# 将json格式的文本转化成dict
import json

file = open('train_count.txt', 'r', encoding='utf-8')
txt_list = file.readlines()
file.close()
char_list_dict = list()
for i in txt_list:
    tmp = dict()
    tmp = json.loads(i.strip('\n'))
    char_list_dict.append(tmp)

print(char_list_dict[1])
