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

n = 1                                   #��־λn���ڼ���Ƿ��¼�ɹ�
while n == 1:                           #������¼�ɹ�ʱ����ʾ����������

    username = input('����ѧ��:')
    password = input('��������:')

    url = 'http://10.32.254.11/a70.htm' #Ҫ���ʵ�url
    check = ["��֤�ɹ�ҳ"]              #�ɹ���¼ƥ�������

    data = {}                           #����post��
    data['DDDDD'] = username
    data['upass'] = password
    data['R1'] = '0'
    data['R3'] = '0'
    data['R6'] = '0'
    data['para'] = '00'
    data['0MKKey'] = '123456'
    data = urllib.parse.urlencode(data).encode('gb2312')

    req = urllib.request.Request(url,data)#����
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
    response = urllib.request.urlopen(req)#�õ�response

    html = response.read().decode('gb2312')#����response

    string = re.findall("��֤�ɹ�ҳ",html)#ƥ���ж��Ƿ�ɹ�

    if string == check:
        print("��¼�ɹ�")
        n = 0

    else:
        print("��¼ʧ��,�˻������������")
        print("����������")

