#перевод цифр "арабские - римские"
table_roman = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def arab_to_roman(number):
    if number <= 0: return ''
    ret = ''
    for arab, roman in table_roman:
        while number >= arab:
            ret += roman
            number -= arab
    return ret


def roman_to_arab(txt):
    txt = txt.upper()
    ret = 0
    for arab, roman in table_roman:
        while txt.startswith(roman):
            ret += arab
            txt = txt[len(roman):]
    return ret


for i in (0, 4, 8, 9, 14, 46, 99, 583, 888, 1668, 1989, 2009, 2015, 2088, 2999):
    arab = arab_to_roman(i)
    roman = roman_to_arab(arab)
    print(i, arab, roman)
    
# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления - в лексикографическом порядке.
def word_counter():
    result = {}
    for line in open("d:/projects/test/input.txt", "r", encoding="utf-8"):
        for word in line.split():
            result[word] = result.get(word, 0) + 1  # вместо этого можно использовать setdefault или defaultdict
    # меняем местами
    result = [(v, k) for k, v in result.items()]
    # сортировка будет автоматически сначала по первому значению, затем по второму
    result = sorted(result, reverse=True)
    print(*[t[1] for t in result], sep='\n')

word_counter()

# Частота каждого символа в строке
test = "Справа из леса вышли двое, ступили на обочину и остановились, глядя в мою сторону. Один из них поднял руку"

all_freq = {}
for s in test:
    if s in all_freq:
        all_freq[s] += 1
    else:
        all_freq[s] = 1
print("Частота символов в строке:\n " + str(all_freq))

# Частота каждого символа в строке из файла
import re

frequency = {}
f = open('d:/projects/test/test.txt', 'r', encoding='utf-8')
text_string = f.read().lower()
match_pattern = re.findall(r'\b[а-я]{1,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])
f.close()

