class ArrayStack :

    def __init__(self) :
        self.size = 0
        self.data = list()
    
    def push(self, data) :
        try:
            if data.isdigit():
                data = int(data)
            elif data.replace(".", "", 1).isdigit():
                data = float(data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(data)
            self.size += 1

    def pop(self) :
        try :
            popData = self.data.pop()
            self.size -= 1
            return popData
        except :
            print("Underflow: Cannot pop data from an empty list")
            return None
    
    def is_empty(self) :
        return not bool(self.data)
    
    def get_stack_top(self) :
        try :
            data = self.data.pop()
            self.data.append(data)
            return data
        except :
            print("Underflow: Cannot get stack top from an empty list")
            return None
    
    def get_size(self) :
        return len(self.data)
    
    def print_stack(self) :
        print(self.data)

def main() :
    text = input()
    circle = ArrayStack()
    square = ArrayStack()
    curly = ArrayStack()
    status = True

    for i in text :
        if i in "(" :
            circle.push(i)

        if i in ")" :
            if circle.is_empty() :
                status = False
            circle.pop()



        if i in "[" :
            square.push(i)

        if i in "]" :
            if square.is_empty() :
                status = False
            square.pop()



        if i in "{" :
            curly.push(i)

        if i in "}" :
            if curly.is_empty() :
                status = False
            curly.pop()

    if curly.get_size() + square.get_size() + circle.get_size() > 0 :
        status = False
    return status

print(main())