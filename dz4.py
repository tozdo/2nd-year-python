import os
import re

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
