import urllib.request
import re

def lenivo():
    req = urllib.request.Request('http://magazines.russ.ru/ier/')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    zag0 = re.compile('<li><a href="/[a-z]+/">(.*?)</a></li>',flags=re.U | re.DOTALL)
    zag = zag0.findall(html)
    print(zag)
    fw = open('E:\\Documents and Settings\\Люда\\Рабочий стол\\zag.txt','w', encoding = 'utf-8')
    zag_str = ', '.join(zag)
    fw.write(zag_str)
    fw.close()
    return

if __name__ == '__main__':
    lenivo()
