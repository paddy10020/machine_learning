# coding:utf-8
import jieba

a = '我是一个好人'
seg = jieba.cut(a, cut_all=True)
print('/'.join(seg))
