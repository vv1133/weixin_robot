# coding:utf-8
import sys, urllib, urllib2, json
import random
import config

res_unknown = [
    u'我不知道说什么',
    u'请换种说法吧',
    u'你说的我听不懂',
    u'什么？',
    u'What?',
    u'么么哒',
]

def chat(data):
    # data: unicode
    print '[IN] %s' % data
    base_url = 'http://www.tuling123.com/openapi/api'
    url = '%s?key=%s&info=%s&userid=%s' % (base_url, config.tuling_key, data.encode('utf-8'), config.tuling_userid)
    req = urllib2.Request(url)
    req.add_header("apikey", config.tuling_apikey)

    try:
        resp = urllib2.urlopen(req)
        content = resp.read()
        if content:
            res_data = json.loads(content)['text']
    except:
        print "unknown error"
        res_data = random.choice(res_unknown)
    finally:
        print '[OUT] %s' % res_data
        return res_data

if __name__ == "__main__":
    chat("你好")
