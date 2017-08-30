#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-13 19:16:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from bs4 import BeautifulSoup

import requests


html = """
<html>
    <head>
        <title>Page title</title>
    </head>
    <body>
        <p id="firstpara" align="center">
        This is paragraph<b>one</b>.
        </p>
        <p id="secondpara" align="blah">
        This is paragraph<b>two</b>.
        </p>
     </body>
</html> """
#全部URL
#url = "http://chuzu.17zwd.com/?zd=2&fl=all&dx=all&sc=all&page=%s"%(2)
url = "http://chuzu.17zwd.com/?zd=1&fl=all"
#大西豪URL
#url = "http://chuzu.17zwd.com/?zd=2&fl=all&dx=all&sc=%E5%A4%A7%E8%A5%BF%E8%B1%AA"
print "url:"+url
page = requests.get(url).text

#print(page)


soup = BeautifulSoup(page,'html.parser')
# print soup.title
# print "####"*30

# print soup.title.name
# print "####"*30

# print soup.title.string
# print "####"*30

# print soup.title.parent.name
# print "####"*30

# print soup.p
# print "####"*30



# print soup.a
# print "####"*30

tags = soup.body.find_all(class_="infoCont")
#print "LEN:"+str(len(tags))
import time
time_now =  time.strftime("%Y-%m-%d",time.localtime())
iloop = 0
for tag in tags:


	#num
	#print "NUMBER:"+str(iloop)

	#telphone
	tel =  str(tag.find(class_="phone").string)

	#port
	port =  tag.find(class_="content").string

	#date
	date = tag.find(class_="time fl").string
	if date == time_now:
		iloop += 1
		print "num%s,date:%s    ,tel:%s    ,info:%s"%(iloop,date,tel,port)
	#out_str = "日期:%s    ,电话:%s    ,信息:%s"%(tel.decode('utf-8'),port,date)
	#print(out_str)
	#print tag
	#print "##" * 50




