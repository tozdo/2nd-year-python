import urllib.request
import re
import time
import os
from html.parser import HTMLParser

def papki():
    kor = 'E://'
    if not os.path.exists(kor + 'balpravda' + '//plain'):
        os.makedirs(kor + 'balpravda' + '//plain')
    if not os.path.exists(kor + 'balpravda' + '//mystem-xml'):
        os.makedirs(kor + 'balpravda' + '//mystem-xml')
    if not os.path.exists(kor + 'balpravda' + '//mystem-plain'):
        os.makedirs(kor + 'balpravda' + '//mystem-plain') #как-то всё некрасиво выглядит((
    for i in range(2011,2017):
        if not os.path.exists(kor + 'balpravda' + '//plain//' + str(i)):
            os.makedirs(kor + 'balpravda' + '//plain//' + str(i))
        if not os.path.exists(kor + 'balpravda' + '//mystem-xml//' + str(i)):
            os.makedirs(kor + 'balpravda' + '//mystem-xml//' + str(i))
        if not os.path.exists(kor + 'balpravda' + '//mystem-plain//' + str(i)):
            os.makedirs(kor + 'balpravda' + '//mystem-plain//' + str(i))
    
def tut_csv():
    fw = open('E://balpravda//metadata.csv', 'w', encoding = 'utf-8')
    fw.write('path\tauthor\tsex\tbirthday\theaded\tcreated\tsphere\tgenre_f\ttype\ttopic\tchronotop\tstyle\taudience_age\taudience_level\taudience_size\tsource\tpublication\tpublisher\tpubl_year\tmedium\tcountry\tregion\tlanguage')
    fw.close()
              
def tut_kach():
    norm_adr = []
    adr_site = 'http://www.balpravda.ru/node/'
    super_mass = []
    global htmls
    htmls = []
    for s1 in range(47, 1522):
        super_mass.append(adr_site + str(s1))
    for adre in super_mass:
        try:
            req = urllib.request.Request(adre)
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                htmls.append(html)
                time.sleep(2)
        except:
            print('Error at ', adre)
            

def main1():
    texts = []
    papki()
    tut_kach()
    h = HTMLParser()
    num = 1
    zags = []
    f_csv = open('E://balpravda//metadata.csv', 'a', encoding = 'utf-8')
    f_csv.write('Path\tauthor\tsex\tbirthday\theader\tcreated\tsphere\tgenre_fi\ttype\ttopic\tchronotop\tstyle\taudience_age\taudience_level\taudience_size\tsource\tpublication\tpublisher\tpubl_year\tmedium\tcountry\tregion\tlanguage\n')
    for html in htmls:
        res = re.sub('<a .*</a>', '', html)
        res2 = re.findall('<div class="content clear-block">(.+?)</div>', res, flags = re.DOTALL) #тексты
        row = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\tн-возраст\tн-уровень\tрайонная\t%s\tБалашовская правда\t\t%s\tгазета\tРоссия\tСаратовская область\tru\n'
        for st in res2:
            ist_b = h.unescape(str(st)) #тут текст чистится
            zag = re.findall('<h1 class="title">(.+?)</h1>', html, flags = re.DOTALL) #найдет заголовок в одном хтмле
            zag2 = ''.join(zag)
            dat = re.findall('[0-9]{2}\.[0-9]{2}\.[0-9]{4}', html, flags = re.DOTALL) #дата
            dat2 = ''.join(dat)
            dat3 = dat2[6:]
            url = re.findall('<form action="(.+?)"', html, flags = re.DOTALL)#адрес
            url2 = ''.join(url)
            ress = re.sub('\<(/?[^\>]+)\>','',ist_b) #тут тоже чистится
            adress = 'E://balpravda//plain//'+ dat3 +'//text' + str(num) + '.txt'
            fw = open(adress, 'w', encoding = 'cp1251') #создается файлик, а такая кодировка потому что у меня 2 майстем
            fw.write('@au NoName\n@ti ' + zag2 + '\n@da ' + dat2 + '\n@url ' + 'http://www.balpravda.ru' + url2 + '\n')
            fw.write(ress)
            num += 1
            f_csv.write(row % (adress, 'NoName', zag2, dat2, 'новости', url2, dat3)) #csv пришел и пополняется с каждым прохождением через цикл
    f_csv.close()

def mystem():
    for i in range(2011, 2017):
        inp = "E:\\balpravda\\plain\\" + str(i)
        lst = os.listdir(inp)
        for fl in lst:
            stroka = 'C:\\mystem.exe' + inp + os.sep + fl + 'E:\\balpravda\\mystem-xml\\' + str(i) + os.sep + fl + ' -cnid --format xml --eng-gr'
            stroka2 = 'C:\\mystem.exe' + inp + os.sep + fl + 'E:\\balpravda\\mystem-plain\\' + str(i) + os.sep + fl + ' -cnid --format txt --eng-gr'
            os.system(stroka)
            os.system(stroka2)

if __name__ == '__main__':
    main1()
    mystem()

