class ArrayStack :

    def __init__(self) :
        self.size = 0
        self.data = []
    
    def push(self, data) :
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
            return self.data[-1]
        except :
            print("Underflow: Cannot get stack top from an empty list")
            return None
    
    def get_size(self) :
        return len(self.data)
    
    def print_stack(self) :
        print(self.data)


def priority(operand) :
    match (operand) :
        case "*" | "/" :
            return 1
        case "+" | "-" :
            return 0

def infixToPostfix(expression) :
    stack = ArrayStack()
    postfix = ""
