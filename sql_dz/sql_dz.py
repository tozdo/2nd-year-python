import os
import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    tnum = 1
    if request.args:
        name = request.args['name']
        text = request.args['text']
        file_name = '/home/tozdo/' + name
        f = open(file_name, 'w', encoding = 'utf-8')
        slova = re.findall('[А-Яа-я]+', text)
        for slovo in slova:
            insert = 'INSERT INTO text(tokens, tnum) VALUES (\'' + slovo + '\',\'' + str(tnum) + '\');\n'
            f.write(insert)
            tnum += 1
        f.close()
        return render_template('answer')
    return render_template('index')

def mystem():
    os.system('/home/tozdo/mystem -cnd /home/tozdo/input_text /home/tozdo/output_text')
    return print('mystem ist fertig')

def sql():
    commands = open('/home/tozdo/commands', 'w')
    shablon_1 = 'INSERT INTO text(id, tokens, tnum) VALUES (\''
    shablon_2 = 'INSERT INTO tokens(token, lemma) VALUES (\''
    file = open('/home/tozdo/output_text', 'r')
    i = 0 #eto id
    snum = 1 #eto nomer slovoformi v texte
    mass_tabl2 = []
    for line in file:
        findevka = re.search('([А-Яа-я]+){([А-Яа-я]+)\??}', line)
        try:
            tabl_1 = shablon_1 + str(i) + '\', \'' + findevka.group(1) + '\', \'' + str(snum) + '\');\n'
            commands.write(tabl_1)
            tabl_2 = shablon_2 + findevka.group(1) + '\', \'' + findevka.group(2) + '\');' + '\n'
            mass_tabl2.append(tabl_2)
            i += 1
            snum += 1
        except:
            if len(line) > 2:
                tabl_1 = shablon_1 + str(i) + '\', \'' + line[:1] + '\');' + '\n'
                commands.write(tabl_1)
                i += 1
                continue
    for el in mass_tabl2:
        commands.write(el)
    commands.close()
    return print('commands sind fertig')


def main():
    mystem()
    sql()

if __name__ == '__main__':
    main()
    app.run()
