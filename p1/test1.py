with open('in.txt', 'r') as fin:
    matrix = []
    for line in fin:
        matrix.append(list(map(float, line.split())))

    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i >= j and i + j >= len(matrix) - 1:
                sum += matrix[i][j]
                print(matrix[i][j])
    print(sum)