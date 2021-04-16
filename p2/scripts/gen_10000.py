import random

with open('gen_10000.txt', 'w') as fin:
    fin.write('10000\n')
    for i in range(10000):
        fin.write(str(random.randint(-100000, 100000)) + '\n')