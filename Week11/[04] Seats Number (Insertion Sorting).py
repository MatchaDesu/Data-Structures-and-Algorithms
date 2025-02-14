from json import loads

def insertionSort(unOrderedList, lastIndex) :
    current = 1
    compareTime = 0

    while current <= lastIndex :
        hold = unOrderedList[current]
        walker = current - 1

        while walker >= 0 and (hold[0] < unOrderedList[walker][0] or (hold[0] == unOrderedList[walker][0] and  int(hold[1:]) < int(unOrderedList[walker][1:]))):
            if hold[0] == unOrderedList[walker][0] and int(hold[1:]) > int(unOrderedList[walker][1:]):
                break
            unOrderedList[walker + 1] = unOrderedList[walker]
            walker -= 1
            compareTime += 1
        
        if walker >= 0 :
            compareTime += 1

        unOrderedList[walker + 1] = hold
        current += 1
        print(unOrderedList)
    
    print("Comparison times:",compareTime)

def main() :

    unOrderedList = loads(input())
    lastIndex = int(input())

    insertionSort(unOrderedList, lastIndex)
main()