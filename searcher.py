#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,re,ssl,logging
import urllib
from urllib import request
from models import fanhao,db
from Base import getconfig,json,PHOTO_PATH

__author__ = 'SunCoder'

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.INFO)

ptCode = re.compile(r'<span class="header">識別碼:</span>.*?<span style="color:#CC0000;">(.*?)</span>', re.I | re.S | re.M)
psTitle = re.compile(r'<h3>(.*?)</h3>', re.I | re.S | re.M)
psStarCode = re.compile(r'<div class="star-name"><a href="https://www.javbus.*?star/(.*?)" title=".*?">.*?</a></div>', re.I | re.S | re.M)
psStar = re.compile(r'<div class="star-name"><a href="https://www.javbus.*?star/.*?" title=".*?">(.*?)</a></div>', re.I | re.S | re.M)
ptImg = re.compile(r'<a class="bigImage" href="(.*?)">', re.I | re.S | re.M)

def opener():
    ssl._create_default_https_context = ssl._create_unverified_context
    proxy_handler = request.ProxyHandler({'http': getconfig('proxy','http'),'https': getconfig('proxy','https')})
    topener = request.build_opener(proxy_handler)
    opener.addheaders = [("authority", getconfig('dbweb','url'))]
    # opener.addheaders = [("method", "GET")]
    # opener.addheaders = [("path", "/HEYZO-0282")]
    # opener.addheaders = [("scheme", "https")]
    # opener.addheaders = [("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")]
    # opener.addheaders = [("dnt", "1")]
    # opener.addheaders = [("upgrade-insecure-requests", "1")]
    topener.addheaders = [("user-agent", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36")]
    return topener


def getinfo(fcode, onlyimg=False):
    if not fcode:
        return json(-1, '番号不正确')
    # 解析番号
    if not onlyimg:
        fcode = fcode.strip().upper().encode('utf-8').decode('utf-8')
        match = re.match(r'[0-9a-zA-Z-_]+', fcode)
        if not match:
            return json(-1, '番号不正确')
    # 获取信息
    res = _request(fcode)
    if res['code'] != 0:
        return json(-1, '番号信息获取失败:' + res['msg'])
    resdata = res['data']
    # 保存信息
    resinf = _saveInf(resdata)
    if resinf == None:
        return json(-2, '番号信息保存错误')
    if resinf['code'] != 0: return json(-3, '番号信息保存失败:' + resinf['msg'])
    # 保存图片
    resimg = _saveImg(resdata['imgsrc'], resdata['filename'])
    if resimg == None:
        return json(-4, '图片信息保存错误')
    if resimg['code'] != 0:
        return json(-5, '图片信息保存失败:' + resimg['msg'])

    return json(0, '获取成功', {'code': fcode, 'title': resdata['title'], 'starcode': resdata['starcode'], 'star': resdata['star'], 'imgsrc': resdata['imgsrc'], 'filename': resdata['filename']})


def _saveInf(infoData):
    try:
        fhinfo = fanhao.get(fanhao.code == infoData['code'])
    except fanhao.DoesNotExist:
        fhinfo = fanhao()
    # try:
    fhinfo.code = infoData['code']
    fhinfo.title = infoData['title']
    fhinfo.star = infoData['star'] or '-暂无'
    fhinfo.starcode = infoData['starcode']
    fhinfo.img = infoData['imgsrc']
    fhinfo.fname = infoData['filename']
    # fhinfo.ima = 0
    # fhinfo.updateTime = int(time.time())
    fhinfo.save()
    db.close()
    return json(0)
    # except:
    #     json(-1, '保存失败')


def _saveImg(imgsrc, fname):
    try:
        rs = opener().open(imgsrc, timeout=15)
        rs = rs.read()
    except Exception as e:
        return json(-1, '网络错误:' + str(e))

    fpath = os.path.join(PHOTO_PATH, fname)

    try:
        with open(fpath, 'wb') as op:
            op.write(rs)
    except Exception as e:
        return json(-1, '保存到本地服务器失败:' + str(e))

    return json(0, '保存成功')


def _request(fcode, tims=0):
    url = 'https://'+getconfig('dbweb','url')+'/' + fcode
    logging.info("request:"+url)
    try:
        res = opener().open(url, timeout=20)
        html = res.read()
    except Exception as e:
        return json(-1, '网络错误:' + str(e))
        # tims += 1
        # if tims == 3:
        #     return json(-1, '网络错误')
        # return _request(fcode, tims)

    html = html.decode('UTF-8')
    title = _domatch(psTitle, html)
    starcode = _domatch(psStarCode, html)
    star = _domatch(psStar, html)
    imgsrc = _domatch(ptImg, html)
    filename = fcode + '.jpg'  # os.path.splitext(imgsrc)[1]

    return json(0, ',', {'code': fcode, 'title': title, 'starcode': starcode, 'star': star, 'imgsrc': imgsrc, 'filename': filename})


def _domatch(rec, htmls):
    mh = rec.findall(htmls)
    if mh and len(mh) > 0:
        return mh[0]
    else:
        return ''


if __name__ == '__main__':
    res = getinfo('IPZ-135')
    print(res)
    # try:
    #     res.send(None)
    # except StopIteration as i:
    #     print(i)
