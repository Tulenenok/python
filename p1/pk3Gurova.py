def lenStroke(stroke):
    a = stroke.split()
    engAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    rusAlphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    for elem in a:
        if len(elem) == 1 and elem.lower() not in engAlphabet and elem.lower() not in rusAlphabet:
            a = a[:a.index(elem)] + a[a.index(elem) + 1:]
    return len(a)

fin = open('in.txt', 'r', encoding='utf8')
fout = open('out.txt', 'w', encoding='utf8')

flag = True             # Первое предложение
stroke = ''
min_len = 0
max_len = 0
min_stroke = ''
max_stroke = ''
for line in fin:
    line = line.replace('\n', ' ')
    for elem in line:
        stroke += elem
        if elem in ['.', '!', '?']:
            if flag or lenStroke(stroke) < min_len:
                min_len = lenStroke(stroke)
                min_stroke = stroke
                flag = False

            if lenStroke(stroke) > max_len:
                max_len = lenStroke(stroke)
                max_stroke = stroke
            stroke = ''
fout.write(min_stroke.strip() + '\n')
fout.write(max_stroke.strip() + '\n')
fin.seek(0)

for line in fin:
    line = line.replace('\n', ' ')
    for elem in line:
        stroke += elem
        if elem in ['.', '!', '?']:
            stroke += '(' + str(lenStroke(stroke)) + ')'
            fout.write(stroke.strip() + '\n')
            stroke = ''

# Извините, я не очень поняла, какой вывод вам нужен.
# Если нужно было сделать так, чтобы выводился текст как в исходном файле, но с количеством слов после . то нужно взять этот кусочек кода
# вместо предыдущего цикла
# fin.seek(0)
# for line in fin:
#     for elem in line:
#         stroke += elem
#         if elem in ['.', '!', '?']:
#             stroke += '(' + str(lenStroke(stroke)) + ')'
#             fout.write(stroke.strip())
#             stroke = ''
fout.close()
fin.close()