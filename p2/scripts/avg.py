def findAvg(src):
    with open(src, 'r') as file:
        countNumbers = 0
        sum = 0
        for line in file:
            sum += float(line.strip())
            countNumbers += 1
        return str(sum / countNumbers)

def fillFiles(finput, foutput):
    with open(foutput, 'w') as fin:
        fin.write(findAvg(finput))

for i in range(1, 4):
    for j in [10, 50, 100, 500, 1000, 5000, 10000]:
        fillFiles(f'time_{j}_{i}.txt', f'time_{j}_{i}_avg.txt')