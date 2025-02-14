"From PSCP"
def main() :
    "main"
    d = int(input())
    fastest = 0
    max_fast = 0
    min_time = 0
    v,start = None, None

    for i in range(1,int(input())+1) :
        v,start = input().split()

        if (d-int(start))/int(v) < min_time or not min_time :
            fastest = i
            min_time = (d-int(start))/int(v)
            max_fast = int(v)

        elif (d-int(start))/int(v) == min_time and int(v) > max_fast :
            fastest = i
            min_time = (d-int(start))/int(v)
            max_fast = int(v)

    print(fastest)
main()
