import urllib.request
import re
import html
from collections import Counter

url_1 = ['https://riafan.ru/580708-uchenye-obyasnili-pochemu-nedosyp-opasen-dlya-serdca']
url_2 = ['https://nation-news.ru/228896-uchenye-vyyavili-chto-nedostatok-sna-ploho-vliyaet-na-rabotu-serdca']
url_3 = ['https://rueconomics.ru/210801-uchenye-rasskazali-o-strashnyh-posledstviyah-nedosypa']
url_4 = ['http://letnews.ru/uchenye-nedostatok-sna-vliyaet-na-rabotu-serdca/']

def fu_words1(url_1):
    try:
        for one in url_1:
            page = urllib.request.urlopen(one)
            whole_text = page.read().decode('utf-8')
            html.unescape(whole_text)
            text = re.findall('</strong(.+)</p>', whole_text, re.U | re.DOTALL)
            for i0 in text: #здесь череда бесконечных реплейсов, потому что по-другому не работало ((
                i = i0.lower()
                i2 = i.replace('\xa0',' ')
                i3 =  i2.replace('</p>', '')
                i4 = i3.replace('<p>', '')
                i5 = i4.replace('\n', ' ')
                i6 = i5.replace('.', '')
                i7 = i6.replace(',', '')
                i8 = i7.replace('"', '')
                i9 = i8.replace('«', '')
                i10 = i9.replace('»', '')
                arr_words1 = i10.split(' ')
                words_1 = set(arr_words1)
            global words_1
            global arr_words1  #массив для raz_again()
    except:
        print('Error at', one)
    return words_1

def fu_words2(url_2):
    try:
        for one in url_2:
            page = urllib.request.urlopen(one)
            whole_text = page.read().decode('utf-8')
            html.unescape(whole_text)
            text = re.findall('title="Ученые выявили, что недостаток сна влияет на работу сердца">(.+)Ранее', whole_text, re.U | re.DOTALL)
            for i0 in text:
                i = i0.lower()
                i2 = i.replace('\xa0',' ')
                i3 =  i2.replace('</p>', '')
                i4 = i3.replace('<p>', '')
                i5 = i4.replace('\n', ' ')
                i6 = i5.replace('.', '')
                i7 = i6.replace(',', '')
                i8 = i7.replace('"', '')
                i9 = i8.replace('«', '')
                i10 = i9.replace('»', '')
                arr_words2 = i10.split(' ')
                words_2 = set(arr_words2)
            global words_2
            global arr_words2  #массив для raz_again()
    except:
        print('Error at', one)
    return words_2

def fu_words3(url_3):
    try:
        for one in url_3:
            page = urllib.request.urlopen(one)
            whole_text = page.read().decode('utf-8')
            html.unescape(whole_text)
            text_block = re.findall('<div id="news_content" class="js-mediator-article">(.+)</p>\n<p style="margin-bottom:10px;">', whole_text, re.U | re.DOTALL)
            for el in text_block:
                slova = re.findall('[А-Яа-я]+', el, re.U | re.DOTALL) #сюда положены слова словечки
            text3 = []
            for i0 in slova:
                i = i0.lower()
                text3.append(i)
            words_3 = set(text3)
        global text3  #массив для raz_again()
        global words_3
    except:
        print('Error at ', one)
    return words_3

def fu_words4(url_4):
    try:
        for one in url_4:
            page = urllib.request.urlopen(one)
            whole_text = page.read().decode('utf-8')
            html.unescape(whole_text)
            text_block = re.findall('<div class="entry entry-content">(.+)</p>\n<div class=\'yarpp-related\'', whole_text, re.U | re.DOTALL)
            for el in text_block:
                slova = re.findall('[А-Яа-я]+', el, re.U | re.DOTALL)
            text4 = []
            for i0 in slova:
                i = i0.lower()
                text4.append(i)
            words_4 = set(text4)
            global text4  #массив для raz_again()
            global words_4
    except:
        print('Error at ', one)
    return words_4

def per():  #пересечения
    f_per = open('per.txt', 'w', encoding = 'utf-8')
    mass_per = []  #будет массив с результатами, чтобы потом его отсортировать
    result_per = words_1 & words_2 & words_3 & words_4
    for slovo in result_per:
        mass_per.append(slovo)
    mass_per.sort()
    for slovo1 in mass_per:
        f_per.write(slovo1 + '\n')
    f_per.close()
    return

def raz():   #симметрическая разность
    f_raz = open('raz.txt', 'w', encoding = 'utf-8')
    mass_raz = []
    result_raz = words_1 ^ words_2 ^ words_3 ^ words_4
    global result_raz
    for slovo in result_raz:
        mass_raz.append(slovo)
    mass_raz.sort()
    for slovo1 in mass_raz:
        f_raz.write(slovo1 + '\n')
    f_raz.close()
    return

def raz_again():
    cw1 = Counter(arr_words1) #словарик, где пары (слово, кол-во)
    moon = [] #массив для частотных слов в статьях
    for i, m in cw1.items():
        if m > 1:  #если слово встречается больше 1-го раза
            moon.append(i)
    cw2 = Counter(arr_words2)
    for i, m in cw2.items():
        if m > 1:  
            moon.append(i)
    cw3 = Counter(text3)
    for i, m in cw3.items():
        if m > 1:  
            moon.append(i)
    cw4 = Counter(text4)
    for i, m in cw4.items():
        if m > 1:  
            moon.append(i)
    sun = set(moon) #чтобы убрать повторяющиеся слова
    life = sun & result_raz #цель задания
    f_raz2 = open('again_raz.txt', 'w', encoding = 'utf-8')
    arr_life = []
    for i in life:
        arr_life.append(i)
    arr_life.sort()
    for slovo in arr_life:
        f_raz2.write(slovo + '\n')
    f_raz2.close()
    
def main():
    fu_words1(url_1)
    fu_words2(url_2)
    fu_words3(url_3)
    fu_words4(url_4)
    per()
    raz()
    raz_again()

if __name__ == '__main__':
    main()
