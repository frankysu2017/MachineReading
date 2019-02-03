#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
from collections import Counter
from wordcloud import WordCloud
import xlrd, xlwt
import operator
import os
import matplotlib.pyplot as plt

jieba.load_userdict(r"./newdict")


def stopwordslist():
    stopwords = [line.strip() for line in open(r'./stopwords', encoding='utf8')]
    stopwords.append('\n')
    stopwords.append(' ')
    return stopwords


def stat_xls(filename):
    xlsbook = xlrd.open_workbook(r'./test.xlsx', )


def text_cloud(filename):
    '''
    show the article in word cloud
    '''
    with open(filename, 'r', encoding='gbk') as f:
        title = f.readline().strip().replace(' ', '\n').replace('：', '\n')
        s = f.read()
        wordcut = [item for item in jieba.cut(s, cut_all=False) if item not in stopwordslist() and len(item)>1]
        cloudtext = ','.join(wordcut)
        wc = WordCloud(
            background_color='white',  # 背景颜色
            max_words=20,  # 显示最大词数
            font_path='./qihei55.ttf',
            min_font_size=30,
            max_font_size=150,
            width=1280,
            height=768
        )
        wc.generate(cloudtext)
    return wc, title


def wordcloud_update(filelist):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.ion()
    articlelist = []
    for file in filelist:
    #i = 0
    #while i < 100:
        #file = filelist[i%len(filelist)]
        #i += 1
        wc, title = text_cloud(r'./news/%s' %file)
        articlelist.append((wc, title))
    for article in articlelist:
        font = {'fontsize': '20', 'fontweight': 'bold', 'verticalalignment': 'baseline', 'horizontalalignment': 'center'}
        plt.title(article[1], fontdict=font, color='red')
        plt.imshow(article[0])
        plt.pause(1)
    plt.cla()
    plt.imshow(plt.imread(r'./end.png'))
    plt.pause(0)


def text_to_bar(filename):
    with open(filename, 'r', encoding='gbk') as f:
        title = f.readline().strip().replace(' ', '\n').replace('：', '\n')
        s = f.read()
        wordcut = [item for item in jieba.cut(s) if item not in stopwordslist() and len(item)>1]
    c = Counter(wordcut)
    topT = dict(reversed(sorted(c.items(),key=operator.itemgetter(1), reverse=True)[:10]))
    return topT, title


def textbar_update(filelist):
    articlelist = []
    for file in filelist:
        topT, title = text_to_bar(r'./news/%s' %file)
        articlelist.append((topT, title))

    plt.figure(figsize=[7.5,6])
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    for article in articlelist:
        font = {'fontsize': '20', 'fontweight': 'bold', 'verticalalignment': 'baseline', 'horizontalalignment': 'center'}
        plt.title(article[1], fontdict=font, color='red')
        plt.barh(range(len(article[0])), list(article[0].values()), tick_label=list(article[0].keys()))
        for x, y in zip(list(article[0].values()), range(len(article[0]))):
            plt.text(x+0.03*max(article[0].values()), y, '%d'%x, ha='center', va='bottom', fontsize=10.5)
        plt.pause(1)
        plt.cla()
    plt.imshow(plt.imread(r'./end.png'))
    plt.pause(0)




if __name__ == "__main__":
    filelist = os.listdir(r'./news')
    # textbar_update(filelist)
    # show dynamic pic
    wordcloud_update(filelist)