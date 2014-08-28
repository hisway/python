#!/usr/bin/python  
# -*- coding: utf-8 -*- 
import urllib, urllib2, cookielib, sys, json ,re, random, threading, time

class index:
    prefix = ''
    suffix = ''
    cookie = None

    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix
        
    def search(self):

        try:
            req = urllib2.Request(url='http://121.14.68.25:8081/domain/search.do?method=findDomainList&searchRandom=1&prefix='+self.prefix+'&suffix='+self.suffix)
            response = urllib2.urlopen(req).read()
        except Exception, e:
            print "网络链接错误"
            return False

        pp = response.split('(')[1].split(')')[0]
        l = json.loads(pp)
        if l[0]['result'][0]['yes'] == []:
            print self.prefix+self.suffix+'已注册'
        else:
            print self.prefix+self.suffix+'未注册'
            # 未注册的写到某个文件中
            f=open(r'cn.txt','a')
            f.write(self.prefix+self.suffix+'\n')
            f.close()


if __name__ == '__main__':
	# 生成n个随机字符
    def getstr(n): 
        st = '' 
        while len(st) < n: 
          temp = chr(97+random.randint(0,25)) 
          if st.find(temp) == -1 : 
            st = st.join(['',temp]) 
        return st
    #随机n次
    def run(n):
        for i in range(n):
            rs = index(getstr(3), '.cn').search()
    #多线程，每个线程运行10000次
    #t11 = threading.Thread(target=run,args=(10000,)).start()
    #t12 = threading.Thread(target=run,args=(10000,)).start()

    # 从打开文件中一行一个查找
    for line in open("word.txt"):
        rs = index(line.strip(), '.cn').search()
        #time.sleep(0.5)





