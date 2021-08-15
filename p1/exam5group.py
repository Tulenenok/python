def getLine(f):
    return f.readline()

def getLineByNumber(n, f):
    line = getLine(f)
    i = 1
    while i != n:
        line = getLine(f)
        i += 1
    f.seek(0)
    return line

def countEventOdd(x):
    odd = 0
    even = 0
    while x > 0:
        if x % 2 == 1:
            odd += 1
        else:
            even += 1
        x //= 10
    if even > odd:
        return True
    return False

with open('in1.txt', 'r') as fin1, open('in2.txt', 'r') as fin2, open('out.txt', 'w') as fout:
    for line in fin1:
        number = int(line.replace('\n', ''))
        newLine = getLineByNumber(number, fin2)
        firtNum, secondNum = map(int, newLine.replace('\n', '').split())
        sumNum = firtNum + secondNum
        if countEventOdd(sumNum):
            fout.write(str(firtNum + secondNum) + '\n')