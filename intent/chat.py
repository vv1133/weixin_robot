# coding:utf-8
import sys, urllib, urllib2, json
import random
import base

class ChatIntention(base.BaseIntention):
    base_url = 'http://www.tuling123.com/openapi/api'
    key = '******************'
    userid = '*******'
    apikey = '***********************'
    res_unknown = [
            u'我不知道说什么',
            u'请换种说法吧',
            u'你说的我听不懂',
            u'什么？',
            u'What?',
            u'么么哒',
            ]

    @classmethod
    def match(cls, data):
        return True

    @classmethod
    def process(cls, data):
        # data: unicode
        print '[IN] %s' % data
        url = '%s?key=%s&info=%s&userid=%s' % (cls.base_url, cls.key, data.encode('utf-8'), cls.userid)
        req = urllib2.Request(url)
        req.add_header("apikey", cls.apikey)

        try:
            resp = urllib2.urlopen(req, timeout=3)
            content = resp.read()
            if content:
                res_data = json.loads(content)['text']
        except:
            print "unknown error"
            res_data = random.choice(cls.res_unknown)
        finally:
            print '[OUT] %s' % res_data
            return res_data

if __name__ == "__main__":
    ChatIntention.process(u"你好")
