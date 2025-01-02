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
    "Testcase"
    stack = int(input())
    student = int(input())
    placeholder = ArrayStack()
    mainStack = list()
    count = 0

    for i in range(stack) :
        mainStack.append(ArrayStack())

    for i in range(student) :
        placeholder.push(input())

    while not placeholder.is_empty() :
        for i in mainStack :
            if count >= student or placeholder.is_empty() :
                break
            i.push(placeholder.pop())
            count += 1
    
    count = 0

    for i in mainStack :
        count += 1
        print(f"Group {count}:",end=" ")
        print(*i.data, sep=", ")
    
main()