def onetwo(n) :
    text = ""
    if n == 1 :
        return "1"
    if n == 2 :
        return "2"
    text += onetwo(n-1) + onetwo(n-2)
    return text

def main() :
    result = onetwo(int(input()))
    print(result)
main()
