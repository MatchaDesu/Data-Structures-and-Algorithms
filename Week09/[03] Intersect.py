from json import loads
import random
from time import time

def is_intersect(list1, list2, list3) :

    list1.sort()
    list2.sort()
    list3.sort()

    i, j, k = 0, 0, 0
    while i < len(list1) and j < len(list2) and k < len(list3) :
        
        if list1[i] == list2[j] == list3[k] :
            return True

        min_value = min(list1[i], list2[j], list3[k])

        if list1[i] == min_value :
            i += 1

        if list2[j] == min_value :
            j += 1

        if list3[k] == min_value :
            k += 1
        
    return False

print(is_intersect(loads(input()), loads(input()), loads(input())))
