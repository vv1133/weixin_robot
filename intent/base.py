# coding:utf-8

class BaseIntention(object):
    @classmethod
    def match(cls, data):
        pass

    @classmethod
    def process(cls, data):
        pass


