#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import execjs
import requests
from scrapy import Selector


id = '144796165342208436'

url = 'https://waimai.meituan.com/qualification/{}'.format(id)

headers = {
    "Host": "waimai.meituan.com",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Referer": "https://waimai.meituan.com/restaurant/{}".format(id),
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

cookies = {
            '__mta': '88842020.1556632007681.1556632007681.1556632007681.1',
           'w_utmz': '"utm_campaign', 'w_uuid': 'xx1UYEyB_pGfwCQ5lsEWv8OnhfYbujrPTIj0fmePMkWWaayZwG9H0XruhwTNtia_',
           '_lxsdk_cuid': '16a59dfcec5c8-045a8109d6cf83-2d604637-4a574-16a59dfcec5c8',
           '_lxsdk': '16a59dfcec5c8-045a8109d6cf83-2d604637-4a574-16a59dfcec5c8',
           'w_visitid': '0b745a3f-51e3-423a-8016-af0bf4aaf51b',
           '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
           '_ga': 'GA1.3.839613755.1556632006',
           '_gid': 'GA1.3.624271908.1556632006',
           'waddrname': '"%E6%B8%9D%E5%8C%97%E8%8A%B1%E5%8D%89%E5%9B%AD%E8%8A%B1%E5%9C%BA"',
           'w_geoid': 'wm78rfss41nh', 'w_cid': '500112', 'w_cpy': 'yubeiqu',
           'w_cpy_cn': '"%E6%B8%9D%E5%8C%97%E5%8C%BA"',
           'w_ah': '"29.589620903134346,106.51872485876083,%E6%B8%9D%E5%8C%97%E8%8A%B1%E5%8D%89%E5%9B%AD%E8%8A%B1%E5%9C%BA"',
           'JSESSIONID': 'iln1stbtid4b1d3rzf32rhfdj',
           '_lxsdk_s': '16a6e7f6bb8-77a-1f2-45a%7C%7C13'
           }

response = requests.get(url,headers=headers,cookies =cookies,verify = False )
# print(response.text)

selector = Selector(text=response.text)

quali_pics = selector.xpath('//ul[@class="fl"]//img/@src').extract()
address = selector.xpath('//div[@class="rest-info-thirdpart poi-address"]/p[@class="poi-detail-right"]//text()').extract_first()
phone = selector.xpath('//div[@class="telephone"]/p[@class="poi-detail-right"]//text()').extract_first()
name = selector.xpath('//div[@class="na"]//span/text()').extract_first()


savedata = {
    'quali_pics':quali_pics,
    'address':address,
    'phone':phone,
    'name':name,
}

print(savedata)