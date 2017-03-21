# coding:utf-8
# 2-gram
# 读取文本后记录字符的个数，并记录字符前的一个字符出现的次数
import copy
import json

# 不读取的字符
exclude_list = list()
exclude_list.append('\t')
exclude_list.append('.')
exclude_list.append(',')
for i in range(ord('a'), ord('z')+1):
    exclude_list.append(i)

# 读取文件
file = open('train.txt', 'r', encoding='utf-8')
txt = ''
for i in file.readlines():
    txt = txt + i.strip('\n')
file.close()

# 记录读取到的字符
char_list = list()
for i in range(len(txt)):
    tmp = txt[i]
    if tmp in exclude_list:
        pass
    elif tmp in char_list:
        pass
    else:
        char_list.append(tmp)

# 为每个字符建立一个表
txt_dict_list = list()
for i in char_list:
    tmp = {'char': i, 'count': 0}
    txt_dict_list.append(copy.deepcopy(tmp))

for i in range(len(txt)):
    tmp = txt[i]
    for j in txt_dict_list:
        if tmp == j['char']:
            j['count'] += 1
            tmp = txt[i-1]
            if tmp in j.keys():
                j[tmp] += 1
            elif tmp in exclude_list:
                pass
            else:
                j[tmp] = 1

# 去除概率比较低
for i in txt_dict_list:
    key_list = copy.deepcopy(list(i.keys()))
    for j in key_list:
        if not (j == 'count' or j == 'char'):
            rate = int(i[j]) / int(i['count'])
            if rate <= 0.005:
                i.pop(j)


file = open('train_count.txt', 'w', encoding='utf-8')
for i in txt_dict_list:
    # 把得到的结果以json格式输出到txt文本
    jsObj = json.dumps(i, ensure_ascii=False)
    file.write(jsObj + '\n')
file.close()

