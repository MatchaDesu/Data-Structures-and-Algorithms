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

def priority(operand) :
    match (operand) :
        case "*" | "/" :
            return 2
        case "+" | "-" :
            return 1
    return 0

def infixToPostfix(expression) :
    postfix = ""
    stack = ArrayStack()

    for i in expression.replace(" ","") :
        if i.isalnum() :
            postfix += i

        elif i == "(" :
            stack.push(i)
        
        elif i == ")" :
            while stack.get_stack_top() != "(" :
                postfix += stack.pop()
            stack.pop()

        else :
            if stack.is_empty() :
                stack.push(i)
            elif priority(i) > priority(stack.get_stack_top()) :
                stack.push(i)
            else :
                while not stack.is_empty() :
                    if priority(stack.get_stack_top()) >= priority(i) :
                        postfix += stack.pop()
                    else :
                        break
                stack.push(i)

        #print(stack.data)

    while not stack.is_empty() :
        postfix += stack.pop()

    return postfix

print(infixToPostfix(input()))
