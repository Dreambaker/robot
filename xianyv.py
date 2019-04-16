# -*- coding: utf-8 -*-
import codecs

from bs4 import BeautifulSoup
from urllib2 import Request
from urllib2 import urlopen
import time
import random
import re
import os

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def gen_req(url):
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'
            ' AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/35.0.1916.47 Safari/537.36')
    req.add_header('content-type', 'charset=utf8')
    return req


def fish_scrawler(url):
    req = gen_req(url)
    r = urlopen(req).read()
    soup = BeautifulSoup(r, "html.parser")
    # print(soup)
    list = soup.find_all('div', class_="ks-waterfall")
    for info in list:
        try:
            price = info.find('span', class_="price").find('em').get_text()
            location = info.find('div', class_="item-location").get_text()
            desc = info.find('div', class_="item-brief-desc").get_text()
            url = info.find('div', class_="item-pic").find('a').get('href')
            title = info.find('div', class_="item-pic").find('a').get('title')
            dr = re.compile(r'<[^>]+>', re.S)
            title = dr.sub('', title)
            priceStr = ""
            price1 = priceStr.join(price)
            price2 = float(price1)
            price3 = int(price2)

            print(price3)
            print(location)
            print(desc)
            print(url)
            print(title)
        except:
            print('parse error')
            continue
        try:
            if 500<price3 < 1200:
                fpath = os.path.join('download', 'temp.txt')
                with codecs.open(fpath, 'a', encoding='utf-8') as f:
                    f.write(title + '|' + str(price3) + '|' + desc + '|' + location + '|' + url + '\n')

        except Exception, e:
            print('write error')
            continue


def send_email(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
    email_client.quit()


if __name__ == '__main__':
    # url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.mTx4fq&st_trust=1&page='+str(page)+'&q=%D3%CE%D3%BE%BF%A8&ist=1'
    for page in range(1, 100):
        #url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.mTx4fq&st_trust=1&page=' + str(
            #page) + '&q=iphone7&ist=1&divisionId=110100'
        url = 'https://s.2.taobao.com/list/?q=iphone7%20美版%20无锁&search_type=item&_input_charset=utf8'
        fish_scrawler(url)
        second = random.randint(2, 10)
        time.sleep(second)

    #send_email('smtp.163.com', 'yoursendemail', 'yourpassword', 'yourreceviedemail', 'less than 1200', 'annex')
    # contact me by mail playactors@163.com for any question