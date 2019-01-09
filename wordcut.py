#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xlrd, xlwt


def statOnxls(filename):
    xlsbook = xlrd.open_workbook(r'./test.xlsx', )


def textToCloud(filename):
    with open(filename, 'r') as f:
        s = f.read()
    l = list(jieba.cut(s, cut_all=False))
    c = Counter(l)
    print(c)
    cloudtext = ','.join(l)
    wc = WordCloud(
        background_color='white',  # 背景颜色
        max_words=200,  # 显示最大词数
        font_path='./qihei55.ttf',
        min_font_size=15,
        max_font_size=50,
        width=800  # 图幅宽度
    )
    wc.generate(cloudtext)
    return wc


if __name__ == "__main__":
    wc = textToCloud(r'./test.txt')
    wc.to_file(r"./pic.png")
    plt.imshow(wc)
    plt.axis("off")
    plt.show()