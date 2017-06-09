from pymorphy2 import MorphAnalyzer
import re
import random

morph = MorphAnalyzer()

def get_data():
    with open('1grams-3.txt', 'r', encoding='utf-8') as f:
        slova_ar = [line.split('\t')[1].strip('\n').lower() for line in f.readlines()[:100000]] 
    f.close()
    nforms = {}
    for slov in slova_ar:
        null_c = str(morph.parse(slov)[0].tag).split(' ')[0]
        nform = str(morph.parse(slov)[0].normal_form)
        if null_c in set(nforms.keys()):
            nforms[null_c].append(nform)
        else:
            nl = []
            nl.append(null_c)
            nforms[null_c] = nl
    return nforms


def get_input(base):
    psays = input('Напишите мне что-нибудь: ')
    words_ar = re.findall('[А-Яа-я]+', psays)
    phrase = []
    try:
        for word in words_ar:
            tags = str(morph.parse(word)[0].tag).split(' ')
            #print(tags)
            if 'NPRO' in tags[0]:
                phrase.append(word)
            elif 'CONJ' in tags[0]: 
                phrase.append(word)
            elif 'PRCL' in tags[0]:
                phrase.append(word)
            elif 'PRED' in tags[0]:
                phrase.append(word)
            elif 'PREP' in tags[0]:
                phrase.append(word)      
            else:
                if len(tags) != 1:
                    schtuks = set(tags[1].split(',')) #параметры
                    basword = morph.parse(random.choice(base[tags[0]]))[0].normal_form
                    reword = str(morph.parse(basword)[0].inflect(schtuks).word)
                    phrase.append(reword)
                else:
                    schtuks1 = set(tags[0].split(','))
                    basword = morph.parse(random.choice(base[tags[0]]))[0].normal_form
                    reword = str(morph.parse(basword)[0].inflect(schtuks).word)
                    phrase.append(reword)          
        str_phrase = ' '.join(phrase)
    except:
        str_phrase = 'Что-то пошло не так. Извините. '
    return print(str_phrase)


def main():
    base = get_data()
    get_input(base)


if __name__ == '__main__':
    main()
