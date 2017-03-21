# coding:utf-8
import re
# 将给出的文本信息变成训练资料


class txt_split:
    def __init__(self, train_txt):
        self.train_txt = train_txt
        self.split = re.compile('[,,.,，,。,!,“,”,:,：,《,》,【,】,\t,\n｝]')
        self.txt_list = list()

    def split_txt(self):
        self.txt_list = self.split.split(self.train_txt)

    def show_txt(self):
        print(self.txt_list)


file = open('train')

