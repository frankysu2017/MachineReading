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
fig = plt.figure()


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
        title = f.readline().strip().replace(' ', '\n')
        s = f.read()
        wordcut = [item for item in jieba.cut(s, cut_all=False) if item not in stopwordslist() and len(item)>1]
        #c = Counter(l)
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
    #for file in filelist:
    i = 0
    while i < 100:
        file = filelist[i%len(filelist)]
        i += 1
        wc, title = text_cloud(r'./news/%s' %file)
        font = {'fontsize': '20', 'fontweight': 'bold', 'verticalalignment': 'baseline', 'horizontalalignment': 'center'}
        plt.title(title, fontdict=font, color='red')
        plt.imshow(wc)
        plt.show()
        plt.pause(0.2)


def text_to_bar(filename):
    wordcut = []
    plt.figure("word vec")
    plt.subplot(111)
    for line in open(filename, 'r', encoding='gbk'):
        wordcut += [item for item in jieba.cut(line) if item not in stopwordslist() and len(item)>1]
    c = Counter(wordcut)
    topT = dict(reversed(sorted(c.items(),key=operator.itemgetter(1), reverse=True)[:10]))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.barh(range(len(topT)), list(topT.values()), tick_label=list(topT.keys()))
    for x, y in zip(list(topT.values()), range(len(topT))):
        plt.text(x+2, y, '%d'%x, ha='center', va='bottom', fontsize=10.5)
        plt.title('词频统计Top10')


if __name__ == "__main__":
    filelist = os.listdir(r'./news')


    # show the word count bar
    #for item in filelist:
    #    plot = text_to_bar(r'./news/%s' %item)
    #    plot.show()
    p = plt.figure('word vec', figsize=(15,5))
    ax = plt.subplot(121)
    ax.plot([1,2,3], [2,4,6])
    plt.title('hi')
    print(ax)
    plt.show()
    plt.ion()
    # show dynamic pic
    #wordcloud_update(filelist)