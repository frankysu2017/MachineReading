#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xlrd, xlwt
import numpy as np


def stopwordslist():
    stopwords = [line.strip() for line in open(r'./stopwords', encoding='utf8')]
    return  stopwords


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


def text_to_bar(filename):
    with open(filename, 'r') as f:
        s = f.read()
    l = list(jieba.cut(s))
    c = Counter(l)
    #c = sorted(c)
    #index = np.array(c.values()[:5])
    print(c)
    #plt.bar(left=0,bottom=index , width=y, color='yellow',height=0.5, orientation='horizontal')
    #plt.show()

if __name__ == "__main__":
    '''
    # show the word cloud
    wc = textToCloud(r'./test.txt')
    wc.to_file(r"./pic.png")
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    '''
    # show the word count bar
    #text_to_bar(r'./test.txt')
