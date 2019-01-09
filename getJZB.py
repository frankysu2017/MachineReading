#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime

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

if __name__ == "__main__":
    l = getBBSlist()
    df = pd.DataFrame(l, columns=['article_title', 'article_link', 'author', 'postdate', 'replynum', 'readnum'])
    df['postdate'] = df['postdate'].apply(pdtime)
    df.to_excel(r'./test.xlsx', sheet_name=u'家长帮')
    df = pd.read_excel(r'./test.xlsx')
    print(type(df['postdate'][6]))
