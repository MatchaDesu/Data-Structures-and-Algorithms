from json import loads

def bubbleSort(unOrderedList, lastIndex) :
    current = 0
    compareTime = 0
    sorted = False

    while current <= lastIndex and not sorted :
        walker = lastIndex
        sorted = True

        while walker > current :
            if unOrderedList[walker][0] < unOrderedList[walker - 1][0] or (unOrderedList[walker][0] == unOrderedList[walker - 1][0] and int(unOrderedList[walker][1:]) < int(unOrderedList[walker - 1][1:])):
                sorted = False
                unOrderedList[walker], unOrderedList[walker - 1] = unOrderedList[walker - 1], unOrderedList[walker]
            walker -= 1
            compareTime += 1
        
        current += 1
        print(unOrderedList)


    print("Comparison times:",compareTime)

def main() :

    unOrderedList = loads(input())
    lastIndex = int(input())

    bubbleSort(unOrderedList, lastIndex)
main()