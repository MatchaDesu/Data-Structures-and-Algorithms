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

def is_parentheses_matching(expression) :
    stack = ArrayStack()
    status = True

    for i in expression :
        if i == "(" :
            stack.push(i)

        if i == ")" :
            if stack.is_empty() :
                status = False
            stack.pop()

    if (status == False) or (not stack.is_empty()):
        return False
    return True

def main() :
    expression = input()
    status = is_parentheses_matching(expression)
    if status :
        print("Parentheses in", expression, "are matched")
    else :
        print("Parentheses in", expression, "are unmatched")
    print(status)
main()

