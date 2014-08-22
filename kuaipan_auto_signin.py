#!/usr/bin/python  
#coding:utf-8
import urllib, urllib2, cookielib, sys, json

class kuaipan:
    userName = ''
    password = ''
    cookie = None

    def __init__(self, userName, pwd):
        self.userName = userName
        self.password = pwd
        self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)
        
    def login(self):
        req = urllib2.Request(url='https://www.kuaipan.cn/account_login.htm')
        urllib2.urlopen(req)
        
        postdata = {'username':self.userName,'userpwd':self.password,'isajax':'yes'}
        postdata = urllib.urlencode(postdata)
        print '++++++++登陆++++++++'
        try:
            req = urllib2.Request(url='http://www.kuaipan.cn/index.php?ac=account&op=login', data=postdata)
        except Exception, e:
            print "网络链接错误"
            return False
        response = urllib2.urlopen(req).read()
        l = json.loads(response)
        if (l and l['state'] == '1'):
            print "登录成功,准备签到！"
        else:
            print '登陆失败',l['errcode']
            exit(1)
        return l

    def signIn(self):
        print '++++++++签到++++++++'
        req = urllib2.Request(url='http://www.kuaipan.cn/index.php?ac=common&op=usersign')
        result = urllib2.urlopen(req).read()
        l = json.loads(result)
        if (l and l['state'] == 1) or \
        (l and 0 == l['state'] and l['increase'] * 1 == 0 and l['monthtask'].M900 == 900):
            print "恭喜你签到成功！"
            k = l['increase']*1
            m = l['rewardsize'] * 1
            if (k == 0 and l['monthtask'].M900 == 900):
                print "本月签到积分已领取完成"
            else:
                print "签到奖励积分:%s" % (k)
            if m == 0:
                print "手气太不好了！奖励 0M 空间"
            else:
                print "签到奖励空间：%s" % (m)
        else:
            if (l['state'] == -102):
                print "今天您已经签到过了"
            else:
                print "签到失败，遇到网络错误，请稍后再试！"
        return result
        
    def turnplatel(self):
        print '++++++++抽签++++++++'
        req = urllib2.Request(url='http://www.kuaipan.cn/turnplate/lottery/')
        result = urllib2.urlopen(req).read()
        l = json.loads(result)
        if (l and l['status'] == 'noChance'): 
            print '今天机会已用完'
        else:
            print '抽奖成功'
        return result 


if __name__ == '__main__':
        user = kuaipan('userName', 'pwd')  
        user.login()
        user.signIn()
        user.turnplatel()    