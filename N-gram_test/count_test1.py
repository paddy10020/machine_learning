# coding:utf-8
# 2-gram
# 记录'国'在文章的次数以及'国'字前面的字
import copy

file = open('train.txt', 'r', encoding='utf-8')
txt_list = file.readlines()
txt = ''
for i in txt_list:
    txt = txt + i.strip('\n')
file.close()

# count_char = '国'
txt_dict = {'main':'国','count':0}
for i in range(len(txt)):
    tmp = txt[i]
    if txt_dict['main'] == tmp:
        txt_dict['count'] += 1
        tmp = txt[i-1]
        # 判断关键字是否存在
        if tmp in txt_dict.keys():
            txt_dict[tmp] += 1
        elif tmp == '\t':
            pass
        else:
            txt_dict[tmp] = 1


key_list = copy.deepcopy(list(txt_dict.keys()))

for i in key_list:
    if not (i == 'count' or i == 'main'):
        rate = int(txt_dict[i]) / int(txt_dict['count'])
        # print(rate)
        if rate <= 0.005:
            txt_dict.pop(i)

print(txt_dict)


