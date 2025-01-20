import json
my_list = json.loads(input())
least = my_list[0]
most = my_list[0]
total = 0

for i in my_list :
    if i > most :
        most = i
    elif i < least :
        least = i
    total += i

print(f"({most:.2f}, {least:.2f}, {total / len(my_list):.2f})")
