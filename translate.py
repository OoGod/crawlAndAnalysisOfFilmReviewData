from lxml import etree
import requests
import json
import sys

def translate(a):
    url='https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=0&tsel=0&kc=1&tk=922682.557426&q={}'
    url=url.format(a)
    con=requests.get(url)
    t=json.loads(con.text)
    return t[0][0][0]

if __name__=="__main__":
    
    a = 'loser'
    b = sys.argv[1] if len(sys.argv)>1 else a
    tra = translate(b)
    print(tra)
