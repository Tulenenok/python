class Segment:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def getStart(self):
        return self.__start

    def getEnd(self):
        return self.__end

    def getLength(self):
        return abs(self.__start - self.__end)

def ans(listOfSegments):
    sum = 0
    SegStart = listOfSegments[0].getStart()
    SegEnd = listOfSegments[0].getEnd()
    flag = True
    for i in range(1, len(listOfSegments)):
        Segment = listOfSegments[i]
        if Segment.getStart() < SegEnd and Segment.getEnd() <= SegEnd:
            flag = True
        elif Segment.getStart() <= SegEnd and Segment.getEnd() > SegEnd:
            SegEnd = Segment.getEnd()
            flag = True
        elif Segment.getStart() > SegEnd:
            listOfSegments = listOfSegments[i:]
            flag = False
            sum += SegEnd - SegStart + ans(listOfSegments)
            break
    if flag:
        sum += SegEnd - SegStart
    return sum

def inputSegmentByConsole(i):
    start = float(input('Введите начало отрезка №' + str(i) + ': '))
    end = float(input('Введите конец отрезка №' + str(i) + ': '))
    return Segment(start, end)

n = int(input('Введите количество отрезков: '))
allSegments = []
for i in range(n):
    newSegment = inputSegmentByConsole(i)
    allSegments.append(newSegment)

allSegments = sorted(allSegments, key=lambda i: i.getStart())
print(ans(allSegments))
