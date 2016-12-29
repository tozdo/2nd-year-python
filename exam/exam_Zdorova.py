import urllib.request
import re
import os

def zad1():
    url = 'http://web-corpora.net/Test2_2016/short_story.html'
    s_slova = [] #массив со словами на с
    try:
        page = urllib.request.urlopen(url)
        whole_html = page.read().decode('utf-8')
        slova_cyr = re.findall('[А-Яа-я]+', whole_html)
        for slovo in slova_cyr:
            if slovo.startswith('с') or slovo.startswith('С'):
                print(slovo)
                s_slova.append(slovo)
    except:
        print('error zad1')
    file_s = open('files.txt', 'w', encoding = 'utf-8') #файл со словами на с
    for slovo in s_slova:
        file_s.write(slovo + '\n')
    file_s.close()
    return print('zad1 done')

def zad2():
    file_v = open('filev.txt', 'w', encoding = 'utf-8') #файл с глаголами
    os.system('C:\\Users\\student\\Desktop\mystem.exe files.txt output.txt -nid')
    output = open('output.txt', 'r', encoding = 'utf-8')
    verbs = []
    for line in output:
        verb = re.findall('{([А-Яа-я]+)=V', line)
        verbs.append(verb)
    for el in verbs:
        for verb in el:
            if el == '':
                continue
            else:
                print(verb)
                file_v.write(verb + '\n')
    file_v.close()
    output.close()
    return(print('zad2 done'))

def zad3():
    shabl = 'INSERT INTO stable(id, lemma, token, pos) VALUES(\''
    soed = '\', \''
    mystemma = open('output.txt', 'r', encoding = 'utf-8')
    i = 0 #id
    commands = open('inserts.txt', 'w', encoding = 'utf-8')
    commands.write('CREATE TABLE stable (id, lemma, token, pos);\n') #чтобы таблица была...
    for line in mystemma:
        result = re.search('([А-Яа-я]+){([а-я]+)\??=([A-Z]+)', line)
        token = result.group(1)
        lemma = result.group(2)
        pos = result.group(3)
        commands.write(shabl + str(i) + soed + lemma + soed + token + soed + pos + '\');\n')
        i += 1
    commands.close()
    mystemma.close()
    return(print('zad3 done'))
    
    
if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
