# coding:utf-8
import intent

def run(data):
    for intention in intent.intentions:
        if intention.match(data):
            return intention.process(data)
    else:
        return None

if __name__ == "__main__":
    run(u"你好")
