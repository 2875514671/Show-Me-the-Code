#! /usr/bin/env python
#coding=utf-8

import requests


def translate(words):
    import re
    url = ("http://translate.google.cn/translate_a/t?"
    "client=t&hl=zh-CN&sl=en&tl=zh-CN&ie=UTF-8&oe=UTF-8&oc=1&otf=2&ssel=3&tsel=0&sc=1&q=%s")
    ret = requests.get(url % words)
    if ret.status_code == 200:
        RULE_TRANSLATE = re.compile('''([^\[\]]+?)\]\]''')
        match = RULE_TRANSLATE.search(ret.text)
        t, o, s, _ = match.group(1).split(u",")
        print(u"����:", t[1:-1])
        print(u"����:", s[1:-1])
        print("")
    else:
        raise Exception("Google�������״̬���쳣��")

 

def tts(words):
    import subprocess
    url = "http://translate.google.cn/translate_tts?ie=UTF-8&q=%s&tl=en&total=1&idx=0&textlen=4&prev=input"
    ret = requests.get(url % words)
    if ret.status_code == 200:
        ext = ret.headers["content-type"].split("/")[1]
        filename = "tts.%s" % ext
        with open(filename, "wb") as f:
            f.write(ret.content)
        # ����ʾmplayer�����
        log_file = "./mplayer.log"
        with open(log_file, "w") as f:
            subprocess.call(["mplayer", filename], stdout=f, stderr=f)
    else:
        raise Exception("Google TTS����״̬���쳣��")


def main(use_tts=False):
    while 1:
        #��window��raw_input����ֱ����ʾ���ģ���Ҫu"����".encode("gbk")
        #Ϊ����ƽ̨�޹أ�����ֱ����ʾ"English:"
        words = raw_input("English:")
        if words == "x":
            break
        if use_tts:
            tts(words)
        translate(words)


if __name__ == "__main__":
    main(use_tts=False)

