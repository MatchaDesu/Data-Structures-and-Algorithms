def pinging(start, stop) :
    if start < stop :
        print(start)
        pinging(start+1, stop)
    elif start > stop :
        print(start)
        pinging(start-1, stop)
    else :
        print(start)
        return

pinging(int(input()), int(input()))