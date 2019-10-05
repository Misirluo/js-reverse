#!/usr/bin/env python
# encoding: utf-8
'''
@author: Misirluo
@contact: misirluo@outlook.com
@file: mtwm_token_reverse.py
@time: 2019-10-05 9:15
@desc:mtwm的token反转文件

'''

# -*- coding: utf-8 -*-

import zlib, re
import gzip
import json
import uuid
import time
import base64
import gzip
import string
import random
import datetime
from requests import request
from requests.utils import unquote
from requests.models import urlencode
from collections import OrderedDict





# result ='IjZMK1U1WnVlUGpvOEwyZGxkR3h2WTJGc1kybDBlV2xrUDJ4aGREMHlPUzQxTXpVNU9EY21iRzVuUFRFd05pNDFNVEl6TURNbVkyOXZjbVJVZVhCbFBUSW1ZMkZzYkdKaFkyczlWMmhsY21WQmJVa3hNVFUwTWpBNE5EQTRNREl3TkQ0NlBERTFOREl3T0RRd09EQTBOVEZkWDFzPSI='
#
# # # ranint = random.randint(1111,9999)
# # # '返回>:</getlocalcityid?lat={}&lng={}&coordType=2&callback=WhereAmI1{}>:<{}]_['.format(lat,lng,stamptime-ranint,stamptime)
# #
# result = unquote(result)
# # print(result)
# a = base64.b64decode(result)
# print(a)
# resultencode = zlib.decompress(a)
# resultencode = base64.b64decode(result)
# print(resultencode)


# print(re.findall(r'callback=(.*)',resultencode)[0])
# result = unquote(resultencode.decode())
# print(result)
# 返回>:</statictest/logevent?name=WhereAmIFail&info=html-[{"code":1,"message":"User denied Geolocation"}]&callback=WhereAmI11542087995801>:<1542088013224]_[
# result = '返回>:</getlocalcityid?lat=29.535987&lng=106.512303&coordType=2&callback=WhereAmI11542084080204>:<1542084080451]_['
# res = base64.b64encode(result.encode()).decode()
# print(res)
# stamptime = time.time()
# print(int(stamptime*1000))

result = 'eyJzeXN0ZW0iOnsiZXJyTXNnIjoiZ2V0U3lzdGVtSW5mbzpvayIsIm1vZGVsIjoiaVBob25lIDUiLCJwaXhlbFJhdGlvIjoyLCJ3aW5kb3dXaWR0aCI6MzIwLCJ3aW5kb3dIZWlnaHQiOjQ1Niwic3lzdGVtIjoiaU9TIDEwLjAuMSIsImxhbmd1YWdlIjoiemgiLCJ2ZXJzaW9uIjoiNi42LjMiLCJzY3JlZW5XaWR0aCI6MzIwLCJzY3JlZW5IZWlnaHQiOjU2OCwiU0RLVmVyc2lvbiI6IjIuNi41IiwiYnJhbmQiOiJkZXZ0b29scyIsImZvbnRTaXplU2V0dGluZyI6MTYsImJhdHRlcnlMZXZlbCI6MTAwLCJzdGF0dXNCYXJIZWlnaHQiOjIwLCJwbGF0Zm9ybSI6ImRldnRvb2xzIiwibmV0d29ya1R5cGUiOiJ3aWZpIn0sImFwcCI6MCwibG9jYXRpb24iOnsibGF0aXR1ZGUiOjI5LjU2NDcxLCJsb25naXR1ZGUiOjEwNi41NTA3Mywic3BlZWQiOi0xLCJhY2N1cmFjeSI6NjUsInZlcnRpY2FsQWNjdXJhY3kiOjY1LCJob3Jpem9udGFsQWNjdXJhY3kiOjY1LCJlcnJNc2ciOiJnZXRMb2NhdGlvbjpvayJ9fQ=='

def detoken(result):
    token_dict = {}
    result = unquote(result)
    resultencode = base64.b64decode(result.encode())
    print(resultencode)
    third = zlib.decompress(resultencode)
    signdict = json.loads(third.decode())
    print(third)
    seventh = signdict.get('sign').encode()
    ningth = zlib.decompress(base64.b64decode(seventh))
    final = ningth.decode().replace('"', '').split('&')
    signdict.pop('sign')
    for eve in final:
        a = re.findall(r'(.*)=(.*)', eve)[0]
        token_dict[a[0]] = a[1]
    return signdict, token_dict

resultfin = detoken(result)
print(resultfin)




# code = b'{"system":{"errMsg":"getSystemInfo:ok","model":"iPhone 6","pixelRatio":2,"windowWidth":375,"windowHeight":555,"system":"iOS 10.0.1","language":"zh","version":"6.6.3","screenWidth":375,"screenHeight":667,"SDKVersion":"2.4.2","brand":"devtools","fontSizeSetting":16,"batteryLevel":100,"statusBarHeight":20,"platform":"devtools","networkType":"wifi"},"location":{"latitude":30.72798,"longitude":106.73043,"speed":1,"accuracy":65,"verticalAccuracy":65,"horizontalAccuracy":65,"errMsg":"getLocation:ok"},"app":0}'
#
#
#
# aaa = base64.b64encode(code).decode()
# print(aaa)

# XWITH='6L+U5ZuePjo8L2dldGxvY2FsY2l0eWlkP2xhdD0yOS41NzcyMjkmbG5nPTEwNi41NDU4MDImY29vcmRUeXBlPTImY2FsbGJhY2s9V2hlcmVBbUkxMTU0NTY0NjY0OTEyMT46PDE1NDU2NDY2NDkyNzNdX1s='




# ranint = random.randint(11111,99999)
# result = str(ranint)+'statictest/loge/vent//?name=&info=htm/l-codemessageUserdeniedeolocation&callback=WhereAmI'+str(time.time())
# wechatFingePrint = base64.b64encode(result.encode()).decode()
# print(wechatFingePrint)
# print(XWITH[0])

# result2 = 'arSAxTit8mJBGIyaL5jaUgHLL325PEICltLE9Bwtm/X7IO4hlYs/OSfM7p+kZAauTlM89vEpLmKiUL0L9iIEuFjm7P6gZ6f7u+Ctv1BJtKefvreNzFQBVOyHeYvnUJMKLfwtoCAAnBDwz/eto6ba70Cn5jReLOWgLVUByg5mmEZKIkYNmTLsR3GnWk6p/CnUQCKhhysVmJ6LheioKbO8/r9SGkib7FmXkS36e9bFa81zhRPvgDlqnvbA8miyhN51iHj148EwN9d0zX08Wadhpfz8owYcjCpgtzRFXR4T04JzG7dwwPN0ibwgYRlAQBB5POCeWcHyRsHmg+etJikRuCkVynreGZicimEIfmSJkjqI90ElhN3ORgt3CEZ7EuIm5zd6sLhoWQjEfKknls1QpyZrmGs5lY1vQXXWbn5UxQen4K0bVIw5Ick4Q4795Ze0PNeyNMDcGv3whi1HdD1y7rCWE+dWemZx5Re61x7BZUwTZZMZ1k6JWbe4KFjXowR/'
# #
# result2 = '64e%7C%7C51'
# result = unquote(result2)
# print(result2)

# result = 'eyJzeXN0ZW0iOnsic2NyZWVuV2lkdGgiOjM2MCwiZXJyTXNnIjoiZ2V0U3lzdGVtSW5mbzpvayIsInBpeGVsUmF0aW8iOjMsInN5c3RlbSI6IkFuZHJvaWQgNy4xLjEiLCJiZW5jaG1hcmtMZXZlbCI6OCwid2luZG93V2lkdGgiOjM2MCwiYnJhbmQiOiJTTUFSVElTQU4iLCJzY3JlZW5IZWlnaHQiOjY0MCwidmVyc2lvbiI6IjYuNi41IiwiZm9udFNpemVTZXR0aW5nIjoxNiwibGFuZ3VhZ2UiOiJ6aF9DTiIsIndpbmRvd0hlaWdodCI6NTYwLCJtb2RlbCI6Ik9EMTAzIiwicGxhdGZvcm0iOiJhbmRyb2lkIiwiU0RLVmVyc2lvbiI6IjEuOS45NyIsIm5ldHdvcmtUeXBlIjoid2lmaSIsImNvbXBhc3MiOlsiMC4wMDAiLCIwLjAwMCIsIjIzMy40ODIiLCIyMzMuNjcxIiwiMjMzLjgyNyIsIjIzNC4zMzMiLCIyMzQuMjA0IiwiMjMzLjc1NCIsIjIzMy44MTMiLCIyMzMuODk5IiwiMjMzLjg3MiIsIjIzMy45MDgiLCIyMzMuOTMxIiwiMjMzLjk0MSIsIjIzMy45MTgiLCIyMzQuMjUyIiwiMjM0LjI0MyIsIjIzMy44NDQiXSwiYWNjZWxlcm9tZXRlciI6W3sieCI6Ii0wLjAyMCIsInkiOiItMC4wMTciLCJ6IjoiLTAuOTkxIn0seyJ4IjoiLTAuMDIyIiwieSI6Ii0wLjAxOSIsInoiOiItMC45OTEifSx7IngiOiItMC4wMjAiLCJ5IjoiLTAuMDE4IiwieiI6Ii0wLjk5MiJ9LHsieCI6Ii0wLjAyMiIsInkiOiItMC4wMTgiLCJ6IjoiLTAuOTkyIn0seyJ4IjoiLTAuMDE4IiwieSI6Ii0wLjAyMCIsInoiOiItMC45OTIifSx7IngiOiItMC4wMjMiLCJ5IjoiLTAuMDE3IiwieiI6Ii0wLjk5MiJ9LHsieCI6Ii0wLjAxOCIsInkiOiItMC4wMjAiLCJ6IjoiLTAuOTkzIn0seyJ4IjoiLTAuMDI0IiwieSI6Ii0wLjAxNiIsInoiOiItMC45OTIifV19LCJsb2NhdGlvbiI6eyJzcGVlZCI6LTEsImVyck1zZyI6ImdldExvY2F0aW9uOm9rIiwibG9uZ2l0dWRlIjoxMDYuNTI2MDQsInZlcnRpY2FsQWNjdXJhY3kiOjAsImxhdGl0dWRlIjoyOS41OTc4MjIsImFjY3VyYWN5IjoyMCwiaG9yaXpvbnRhbEFjY3VyYWN5IjoyMH0sInVzZXJJbmZvIjp7Im5pY2tOYW1lIjoiemV3ZW4iLCJnZW5kZXIiOjEsImxhbmd1YWdlIjoiemhfQ04iLCJjaXR5IjoiIiwicHJvdmluY2UiOiIiLCJjb3VudHJ5IjoiQmVybXVkYSIsImF2YXRhclVybCI6Imh0dHBzOi8vd3gucWxvZ28uY24vbW1vcGVuL3ZpXzMyL0xGbGtZV29oQ3d5SG1HZkFGck5teTB2TjRLRDIyN0FNcFFaOWF3d2lhT21DcnZ6WnU2YWozRUZoZVBISDBQNkN5ZGlhM1czaEhpYXJnZmtOWm9nak9GSFFBLzEzMiJ9LCJhcHAiOjB9'
#
# resultencode = base64.b64decode(result.encode())
# print(resultencode)
# third = zlib.decompress(resultencode)
# print(third)
#
#
# num = 861112245747325











