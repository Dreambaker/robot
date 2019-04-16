# -*- coding:utf-8 -*-

import os
import requests
from lxml import html

headers = {
    'Host':'www.zhihu.com',
    'Accept-language': 'zh-CN,zh;q=0.6',
    'Accept-Encoding':'gzip,deflate,sdch,br',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests':'1',
    'Accept':'text/html,application/xhtml+xml,application/xml;1=0.9,image/webp,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_12_4)'
                'AppleWebKit/537.36 (KHTML,like Gecko) Chorme/57.0.2987.133 Safari/537.36',
}

def save(text,filename='temp',path='download'):
    fpath = os.path.join(path,filename)
    with open(fpath,'w') as f:
        f.write(text)

def save_image(image_url):
    resp = requests.get(image_url)
    page = resp.content
    filename = image_url.split('zhimg.com/')[-1]
    save(page,filename)
def crawl(zhihu_url):
    resp = requests.get(url,headers=headers)
    page = resp.content
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@data-original]/@data-original')
    print('count:',len(image_urls))
    print(image_urls)
    for image_url in image_urls:
        save(image_url)

if __name__ == '__main__':
    url = 'http://www.zhihu.com/question/27364360'
    crawl(url)




