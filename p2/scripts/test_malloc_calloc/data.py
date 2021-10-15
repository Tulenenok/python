for i in range(1, 3):
    with open(f'data_{i}.txt', 'w') as fout:
        for j in [10, 50, 100, 500, 1000, 5000, 10000]:
            with open(f'time_{j}_{i}_avg.txt') as fin:
                fout.write(f'{j} {fin.read().strip()} \n')