#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time


def getBBSlist():
    url = r'http://www.jzb.com/bbs/forum.php?mod=forumdisplay&fid=3220&typeid=6150&filter=typeid&typeid=6150&page={0}'
    tiplist = []
    for i in range(1, 10):
        page = requests.get(url.format(i))
        soup = BeautifulSoup(page.text, features="lxml")
        for k in soup.find_all(name='tbody', id=re.compile("normalthread_\d*")):
            article = k.find(name='a', attrs={"class": "xst"})
            article_title = article["title"]
            article_link = article["href"]
            by = k.find(name='td', attrs={"class": "by"})
            author = by.cite.a.string
            postdate = by.em.span.string
            num = k.find(name='td', attrs={"class": "num"})
            replynum = num.a.string
            readnum = num.em.string
            tiplist.append([article_title, article_link, author, postdate, replynum, readnum])
    return tiplist


def pdtime(strTime):
    return datetime.strptime(strTime, "%Y-%m-%d")


def genewc(table):
    for item in table[1]['article_title']:
        wordlist = []
        wordlist.extend(list(jieba.cut(item, cut_all=False)))
    c = Counter(wordlist)
    cloudtext = ','.join(wordlist)
    wc = WordCloud(
        background_color='white',  # 背景颜色
        max_words=200,  # 显示最大词数
        font_path='./qihei55.ttf',
        min_font_size=15,
        max_font_size=50,
        width=800  # 图幅宽度
    )
    wc.generate(cloudtext)
    wc.to_file(r"./%s.png" %table[0])
    plt.title(r"%s" %table[0], fontsize='x-large', verticalalignment= 'top', color='red')
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    return wc

if __name__ == "__main__":
    '''
    #get JZB.bbs tips
    l = getBBSlist()
    df = pd.DataFrame(l, columns=['article_title', 'article_link', 'author', 'postdate', 'replynum', 'readnum'])
    df['postdate'] = df['postdate'].apply(pdtime)
    df.to_excel(r'./test.xlsx', sheet_name=u'家长帮')
    '''

    df = pd.read_excel(r'./test.xlsx').set_index('postdate')
    df['yearmonth'] = df.index.year*100+df.index.month
    yearmonth = sorted(set(df['yearmonth']))
    grouped = df.groupby(df['yearmonth'])
    for item in grouped:
        genewc(item)

