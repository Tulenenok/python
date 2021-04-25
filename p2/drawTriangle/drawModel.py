def distance(x, y):
    return ((x[0] - y[0])**2 - (x[1] - y[1])**2)**0.5

def isOneLine(x, y, z):
    d1, d2, d3 = distance(x, y), distance(z, y), distance(x, z)
    print(abs(d1 + d2 - d3))
    print(abs(d3 + d2 - d1))
    print(abs(d1 + d3 - d2))
    if abs(d1 + d2 - d3) < 0.1 or abs(d1 + d3 - d2) < 0.1 or abs(d3 + d2 - d1) < 0.1:
        return True
    return False

def lenSide(firstPoint, secondPoint):
    return ((firstPoint[0] - secondPoint[0]) ** 2 + (firstPoint[1] - secondPoint[1]) ** 2) ** 0.5

def sides(firstPoint, secondPoint, thirdPoint):
    firstSide = lenSide(firstPoint, secondPoint)
    secondSide = lenSide(secondPoint, thirdPoint)
    thirdSide = lenSide(firstPoint, thirdPoint)
    return [firstSide, secondSide, thirdSide]

def lenBisector(firstPoint, secondPoint, thirdPoint):
    a, b, c = sides(firstPoint, secondPoint, thirdPoint)
    p = (a + b + c) / 2
    bisector = 2 * (a * c * p * (p - b))**0.5 / (a + c)
    return bisector

def minThreeElByAttr(list, func):
    min, minEl = None, 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            for k in range(j + 1, len(list)):
                if not isOneLine(list[i], list[j], list[k]):
                    newMin = func(list[i], list[j], list[k])
                    if min == None or newMin < min:
                        min, minEl = newMin, [list[i], list[j], list[k]]
                print("Точки  -- ", list[i], list[j], list[k], ",  длинна биссектрисы  -- ", round(newMin, 4))
    return minEl