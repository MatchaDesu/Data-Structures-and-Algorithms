from json import loads

def selectionSort(unOrderedList, lastIndex) :
    current = 0
    compareTime = 0

    while current <= lastIndex :
        smallest = current
        walker = current + 1

        while walker <= lastIndex :
            if unOrderedList[walker] < unOrderedList[smallest] :
                smallest = walker
            walker += 1
            compareTime += 1

        unOrderedList[current], unOrderedList[smallest] = unOrderedList[smallest], unOrderedList[current]
        current += 1
        if current <= lastIndex :
            print(unOrderedList)
    
    print("Comparison times:",compareTime)

def main() :

    unOrderedList = loads(input())
    lastIndex = int(input())

    selectionSort(unOrderedList, lastIndex)
main()