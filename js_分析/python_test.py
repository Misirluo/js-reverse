#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/3/29 13:02
@contact: luozw@yujialong.com
@file: python.py
@author: yjl

"""

import base64
import os
import requests
import execjs
# from yjl_spider_main.comment.dbs.mongodb_conn import *
# os.environ["NODE_PATH"] = r"D:\Program Files\nodejs\node_modules"






# p = os.popen('node music163.js')
# signature = p.readlines()
#
# print(signature)
# print(type(signature))
# for sign in signature:
#     print(sign)
#     sign = eval(sign)

    # print(sign.get('encText'),sign.get('encSecKey'))



# params = canshu[0].strip()
# encSecKey = canshu[1].strip()

# print(params)
# print(encSecKey)




# encSecKey="22b45c986832eb7044a06b0c155950ef8fbbd71610d0a9ffe07cecc86ccb1d0c1a772c688c02592fcd235305bfcc949a9ad469db295312b5118818c7d43d10ea67a92a2eac723cef542589d99ed3a9785f2f1fecff65cae11ab197d3e8deb7fabd6538b4a9e3dbbb2ae39ad82422a7f717a36d4db0ffb1ff41936ba8882ab9ab"
# # params = "qWJQCZQ3s6NVy8UxnKKSjsOfKz9rSqMd6LsYZ76vabDjgQmO/i1FpDknnq8k9X+VBbxrjp7JP6cmqbIACa0Xj5SplPVwp3702ea7BTsxYU8bPdzMGajoE6m3DM6DIoV94tGNAOItxbrU1WB6pVphaQnOPUkIFf/NxHfusbeKRz8NoC1Ejg1TGKbyZv6CEQuX"
# #           fd6cQPaK4rW9tFKOibp8tt11oud4Uaxv+HzLaUFJH+kioNEvzpfhSIpRzVIjqkhHedOvqhtteu7AR6cp2MajhQ1ULgq7WZgCilHXYUw7khafMl4jMb3BHzEaLas2PbZgjrLD9SlvwVLksiW/e5jOnA2eQLnIfbaHjlRKP6AE0uDsLEFxRUUgKf8YONTeNlFjtSr9n4jLrDhZybZJOKKCGXuVY9b/Eatg3BSMezpPASzDAJMDmGIp07GgL/A4/m7U+A2mz0xz+H93vZSaoZjEqw==
# params = signature[0]
# print(params)
# data = {
#     # 'params':params,
#     'params':params,
#     'encSecKey':encSecKey,
# }
# url = 'https://music.163.com/weapi/artist/top?csrf_token='
# #
# headers = {
# "Accept":"*/*",
# "Accept-Encoding":"gzip, deflate, br",
# "Accept-Language":"zh-CN,zh;q=0.9",
# "Cache-Control":"no-cache",
# "Connection":"keep-alive",
# "Content-Length":"472",
# "Content-Type":"application/x-www-form-urlencoded",
# "Cookie":"_iuqxldmzr_=32; _ntes_nnid=04c7c630b9663f90b0ea89bdb76a11a2,1554045264813; _ntes_nuid=04c7c630b9663f90b0ea89bdb76a11a2; WM_NI=uNZG%2BR7QM2daHrm4e2uMfuJusEO2owb9BYn0YeKi7vlkL9jCksUds17tFmPlYNVosrtQjGDkDukzeU2%2FROyUnuAn8S1IyJraN4SzGPlqjRMHDrk6PcuJiml45ykCtr6lN3c%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea6b33ea3968b98fb67879e8fa3d54e878e9aabf268ed92b8aeb454baeca1baca2af0fea7c3b92ab79296a8aa5af58f83d3e76b8caea3d5e83ab793aa96c97fb19b81d3ee7da2e78ebaed3c9bbb858ab67eb0b584dae949a9ad9b85f23bf5ac8a8ed3689b929a90f27ab88fa6a8c76188aba59be85ff2f19eb0fc5faeab8f8fbb59f397b7abf16b8eec9d9bc65cb0afa6b3d04488aea5d7d369b796a78eef40f7a7a5a4f77af6b482d4e237e2a3; WM_TID=a86vqPLI4yxEFURURQJ51rchM1CzppJb; JSESSIONID-WYYY=XG3oXHiGZH%5ChDHSAtRXtHB0AkxYHJYA2h5lT5q%2FCnkpWZDUuUrZx%2FmF328iEEZjwc2WZWwwG37peoN%2BHCTB%2Bi1Z6Rg6gu%2BwsDj5xewn9d0PDElaSRH04tsp9otUU7cZ0o3Uo93%2BPgNkw5UooFvEHfHCmK%2FF%2B0Sps7ZW%2BcA9CCrf%2FOR1A%3A1554048805548",
# "Host":"music.163.com",
# "Origin":"https://music.163.com",
# "Pragma":"no-cache",
# "Referer":"https://music.163.com/discover/artist/signed/",
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
# }
# #
# response = requests.post(url,data = data,headers = headers,verify = False)
# print(response.status_code)
# print(response.text)
# print(response.json())

# jZwWszizY6vzS5Yb5XcvfacU3kRzpvCU0fKdt+lyuWxed55Ai3p41TFkl4NQsU2rSMMu6bR9voR7d1NVjFj2THBEXBoOC1rd16CXNM+U1/ACm7dcUXxVsfLwCrPKZhuP
# 32a71f87cff9c3166d4b95248165503a9d8928869634304c1a0b5559ee5c26bab42dd3f6a478b9e1034301abf069eb13e6e50e19654529d1dfe6eabc246cceedc8d6c2ba136c350cbd3c620d7f39c7a3


# 38c968407ac6ac0344b0490ad7f5466130e5ece0322cb899eb8c3dcfd931de5f1b485583e8700a0ae01d30e441005c13c0581923f69a31437b879cfe4dffb4083819ee4b8cbe60896ace3d153ab00e563d9e16dc1bc68b3ca2cbbd020c887c4be124ba7cf65f8a288d6c834d034912a032aefe2432e2b961317d834a78c93b76
# 9d13e419aad956a848330285d2feb94ee7ed2b77775267a8960b37711afdcea45ad266f9e6b507012c3fb03a5bfcee3e0cb1276620bb2a53e7498503e493e5b8a423cfc9698406db3bf2f16f2af7b36ff12d69f472305fca1a19b8a1f7975720dcbe6daf9b450b47b73c86804a49b0a75f52a32417ceedbfa69aca96498ad204



# # coding = utf-8
# from Crypto.Cipher import AES
#
# from binascii import b2a_hex, a2b_hex
# import base64
# import requests
# import json
# #
# # headers = {
# #     'Cookie': 'appver=1.5.0.75771;',
# #     'Referer': 'http://music.163.com/'
# #
# #
# # }
#
# first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
# second_param = "010001"
# third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# forth_param = "0CoJUm6Qyw8W8jud"
#
#
# def get_params():
#     iv = "0102030405060708"
#     first_key = forth_param
#     second_key = 16 * 'F'
#     h_encText = AES_encrypt(first_param, first_key, iv)
#     h_encText = AES_encrypt(h_encText, second_key, iv)
#     return h_encText
#
#
# def get_encSecKey():
#     encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
#     return encSecKey
#
#
# def AES_encrypt(text, key, iv):
#     pad = 16 - len(text) % 16
#     text = text + pad * chr(pad)
#     encryptor = AES.new(
#                         key,
#                         AES.MODE_CBC,
#                         iv
#                         )
#     encrypt_text = encryptor.encrypt(text)
#     encrypt_text = str(base64.b64encode(encrypt_text))[2:-1]
#     return encrypt_text
#
#
#
#
# def get_json(url, params, encSecKey):
#     data = {
#         "params": params,
#         "encSecKey": encSecKey
#     }
#     response = requests.post(url, headers=headers, data=data)
#     return response.content
#
#
# if __name__ == "__main__":
#     url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_30953009/?csrf_token="
#     params = get_params()
#     encSecKey = get_encSecKey()
#     json_text = get_json(url, params, encSecKey)
#     json_dict = json.loads(json_text)
#     print(json_dict['total'])
#     for item in json_dict['comments']:
#         print(item['content'].encode('gbk', 'ignore'))