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
    return stopwords


def statOnxls(filename):
    xlsbook = xlrd.open_workbook(r'./test.xlsx', )


def textToCloud(filename):
    with open(filename, 'r') as f:
        s = f.read()
    l = (jieba.cut(s, cut_all=False))
    c = Counter(l)
    #print(c)
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
    wordcut = []
    with open(filename, 'r') as f:
        for line in f:
            l = jieba.cut(line)
            wordcut += [item for item in l if item not in stopwordslist() and len(item) > 1]
    c = Counter(wordcut)
    c = dict(sorted(c.items(), key=lambda x:x[1], reverse=True)[:10])
    print(c.keys())
    plt.bar(x=0, bottom=range(10), width=list(c.values())[::-1], color='skyblue', height=0.5, orientation='horizontal')
    plt.yticks(tuple(range(10)), tuple(list(c.keys())[::-1]))
    plt.show()

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
    text_to_bar(r'./test.txt')
    #print(stopwordslist())
