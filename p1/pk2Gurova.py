n = int(input('Введите количество строк в описании сложенного листа: '))

matrix = []
for i in range(n):
    b = []
    s = input('Введите строку сложенного листа №' + str(i + 1) + ': ')
    for j in range(len(s)):
        b.append(s[j])
    while len(b) < n:
        b.append('+')
    matrix.append(b)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '.':
            matrix[j][i] = '.'
            matrix[n - i - 1][n - j - 1] = '.'
            matrix[n - j - 1][n - i - 1] = '.'

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()

for idx in range(n):
    mi = 0
    minp = n + 1
    i = idx
    while i < n:
        qnt = 0
        for j in range(n):
          if matrix[j][i] == '.':
              qnt += 1
        if qnt < minp:
            mi = i
            minp = qnt
        i += 1
    for i in range(n):
        x = matrix[i][idx]
        matrix[i][idx] = matrix[i][mi]
        matrix[i][mi] = x

print()
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()