#!/bin/sh
sudo python3 /etc/apt/NLogin.py
root@raspberrypi:/home/pi# l
bash: l: command not found
root@raspberrypi:/home/pi# cat /etc/ap
apparmor.d/ apt/
root@raspberrypi:/home/pi# cat /etc/apt/NLogin.py
import urllib.request
import urllib.parse
import re

n = 1                                   #标志位n用于检查是否登录成功
while n == 1:                           #当不登录成功时会提示并重新输入

    username = input('输入学号:')
    password = input('输入密码:')

    url = 'http://10.32.254.11/a70.htm' #要访问的url
    check = ["认证成功页"]              #成功登录匹配的文字

    data = {}                           #构造post包
    data['DDDDD'] = username
    data['upass'] = password
    data['R1'] = '0'
    data['R3'] = '0'
    data['R6'] = '0'
    data['para'] = '00'
    data['0MKKey'] = '123456'
    data = urllib.parse.urlencode(data).encode('gb2312')

    req = urllib.request.Request(url,data)#访问
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
    response = urllib.request.urlopen(req)#得到response

    html = response.read().decode('gb2312')#解码response

    string = re.findall("认证成功页",html)#匹配判断是否成功

    if string == check:
        print("登录成功")
        n = 0

    else:
        print("登录失败,账户名或密码错误")
        print("请重新输入")

