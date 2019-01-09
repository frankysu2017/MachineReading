#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def getBBSlist():
    url = r'http://www.jzb.com/bbs/forum.php?mod=forumdisplay&fid=3220&typeid=6150&filter=typeid&typeid=6150&page={0}'
    page = requests.get(url.format({1}))
    soup = BeautifulSoup(page.text, features="lxml")
    i = 0
    for k in soup.find_all(name='tbody', id = "normalthread_7008745"):
        print(k.th)

if __name__ == "__main__":
    getBBSlist()