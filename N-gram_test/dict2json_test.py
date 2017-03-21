# coding:utf-8

import json

# file = open('dict2json.txt', 'w', encoding='utf-8')
a = {'main': '关耀鹏', 'count': 2}
jsObj = json.dumps(a, ensure_ascii=False)
print(jsObj)
