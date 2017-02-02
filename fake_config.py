# coding:utf-8

token = '1234'
host = '0.0.0.0'
port = 12233
session = True
server = 'tornado'

wx_config = {}
wx_config["APP_ID"] = '************'
wx_config["APP_SECRET"] = '************************'

menu = {
    "button": [
        {
            "type": "click",
            "name": u"首页",
            "key": "main"
        }, {
            "type": "click",
            "name": u"历史推送",
            "key": "ls"
        }, {
            "type": "click",
            "name": u"帮助",
            "key": "help"
        }
    ]
}

