#coding=utf-8
import requests
import json
s = requests.Session()
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}
username = 'username'  # 用户名
password = 'password'  # 密码
 
r = s.get('http://www.smzdm.com/user/login/jsonp_check?user_login=%s&user_pass=%s' % (username, password), headers=headers)  # json验证
resp = json.loads(r.text[1:-1])  # 解析json脚本，其实不用也行
print r.text
print resp
t = s.get('http://www.smzdm.com//user/qiandao/jsonp_checkin', headers=headers)  # json签到
print t.text


