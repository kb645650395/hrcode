#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = "http://www.bluecore.com.cn/"
response = requests.get(url=url)
response.enconde = response.apparent_encoding
r = response.text.replace('\ufeff','')
with open("a.txt","w") as f:
    f.write(r)
