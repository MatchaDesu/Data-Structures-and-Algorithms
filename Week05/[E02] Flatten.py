from json import loads as toList

def flatten(myList) :
    flatted = []
    for i in myList :
        if isinstance(i, list) :
            flatted.extend(flatten(i))
        else :
            flatted.append(i)
    return flatted

def main() :
    result = flatten(toList(input()))
    print(sorted(result,reverse=True))
main()