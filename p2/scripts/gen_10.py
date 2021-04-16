import random

with open('gen_100.txt', 'w') as fin:
    fin.write('10\n')
    for i in range(10):
        fin.write(str(random.randint(-100000, 100000)) + '\n')