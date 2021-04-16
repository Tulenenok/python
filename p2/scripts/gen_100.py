import random

with open('gen_100.txt', 'w') as fin:
    fin.write('100\n')
    for i in range(100):
        fin.write(str(random.randint(-100000, 100000)) + '\n')