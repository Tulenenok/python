import random

with open('gen_1000.txt', 'w') as fin:
    fin.write('1000\n')
    for i in range(1000):
        fin.write(str(random.randint(-100000, 100000)) + '\n')