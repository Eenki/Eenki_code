import urllib.request
import urllib.parse
import re

n = 1                                   
while n == 1:                          
    username = input('Input StudentNumber:')
    password = input('Input Password:')
    url = 'http://10.32.254.11/a70.htm' 
    check = ["认证成功页"]
    data = {}
    data['DDDDD'] = username
    data['upass'] = password
    data['R1'] = '0'
    data['R3'] = '0'
    data['R6'] = '0'
    data['para'] = '00'
    data['0MKKey'] = '123456'
    data = urllib.parse.urlencode(data).encode('gb2312')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('gb2312')
    string = re.findall("认证成功页",html)

    if string == check:
        print("Successfully")
        n = 0

    else:
        print("failed!")

