#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xlrd, xlwt
import numpy as np
import operator
jieba.load_userdict(r"./newdict")

def stopwordslist():
    stopwords = [line.strip() for line in open(r'./stopwords', encoding='gbk')]
    stopwords.append('\n')
    stopwords.append(' ')
    return stopwords


def statOnxls(filename):
    xlsbook = xlrd.open_workbook(r'./test.xlsx', )


def textToCloud(filename):
    '''
    show the article in word cloud
    '''
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
    wordcut = []
    for line in open(filename, 'r', encoding='utf8'):
        wordcut += [item for item in jieba.cut(line) if item not in stopwordslist() and len(item)>1]
    #print(wordcut)
    c = Counter(wordcut)
    topT = dict(reversed(sorted(c.items(),key=operator.itemgetter(1), reverse=True)[:10]))
    #print(c)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.barh(range(len(topT)), list(topT.values()), tick_label=list(topT.keys()))
    for x, y in zip(list(topT.values()), range(len(topT))):
        plt.text(x+0.1, y, '%d'%x, ha='center', va='bottom', fontsize=10.5)
    plt.title('词频统计Top10')
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
