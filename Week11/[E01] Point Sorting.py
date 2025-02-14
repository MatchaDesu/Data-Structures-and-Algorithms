def pointValue(point) :
    x, y = point.split()
    return float(x) + float(y)

def getY(point) :
    return float(point.split()[1])

def pointSorting(t) :

    for _ in range(t) :
        orderedPoint = []
        pointAmount = int(input())
        current = 1

        for _ in range(pointAmount) :
            point = input()

            orderedPoint.append(point)

            current = 0
            sorted = False

            while current <= len(orderedPoint) - 1 and not sorted :
                walker = len(orderedPoint) - 1
                sorted = True

                while walker > current :
                    if pointValue(orderedPoint[walker]) < pointValue(orderedPoint[walker - 1]) or \
                        (pointValue(orderedPoint[walker]) == pointValue(orderedPoint[walker - 1]) and getY(orderedPoint[walker]) > getY(orderedPoint[walker - 1])):
                        sorted = False
                        orderedPoint[walker], orderedPoint[walker - 1] = orderedPoint[walker - 1], orderedPoint[walker]
                    walker -= 1
                
                current += 1
        
        print(*orderedPoint, sep="\n")

pointSorting(int(input()))