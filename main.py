# coding:utf-8
import os
from bs4 import BeautifulSoup
import requests

def showinfo(tags):
	#print "LEN:"+str(len(tags))
	import time
	time_now =  time.strftime("%Y-%m-%d",time.localtime())
	iloop = 0
	tag_list = []
	for tag in tags:
		#print(tag)
		#num
		iloop = iloop + 1
		#print "NUMBER:"+str(iloop)

		title = tag.h5.string
		#print (tag.find(class_="sizeCont").string)
		#print(str(iloop)+":"+tag.select(".content")[0].get_text())
		# tag_list.insert(0,str(iloop)+tag.select(".content")[0].get_text())
		content = tag.select(".all-text-content")[0].get_text()
		#print tag.find(class_="phone")
		date =  tag.find(class_="time fl").string

		sizeCont = tag.select(".sizeCont")[0].get_text()

		# #telphoneex
		tel =  tag.select(".phone")[0].get_text()
		#print tel
		# #port
		#port =  tag.select(".content")[0].get_text()
		#print port
		#print port

		# #date
		print "[%s]title:%s,content:%s\t,size:%s\t,date:%s\t,tel:%s\t"%(iloop,title,content,sizeCont,date,tel)
		#out_str = "日期:%s    ,电话:%s    ,信息:%s"%(tel.decode('utf-8'),port,date)
		#print(out_str)
		#print tag
		#print "##" * 50
		#print("==="*6)
	# for i in tag_list:
	# 	print i



def main():
	import time
	urls = []
	urls= ("http://chuzu.17zwd.com/?zd=1&fl=all&page=2","http://chuzu.17zwd.com/?zd=1&fl=all")
	for url in urls:
		print "url:"+url
		page = requests.get(url,timeout=3).text

		#print page
		soup = BeautifulSoup(page,"html.parser")
		tags = soup.body.find_all(class_="infoCont")
		showinfo(tags)

if __name__ == '__main__':
	main()
