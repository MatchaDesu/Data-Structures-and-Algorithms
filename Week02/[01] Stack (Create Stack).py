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
        return self.size
    
    def print_stack(self) :
        print(self.data)

def main():
    stack = ArrayStack()
    text_in = input()
    while text_in.lower() != "exit":
        condition, data = text_in.split(": ")
        if condition == "Push":
            stack.push(data)
        elif condition == "Pop":
            stack.pop()
        elif condition == "Top":
            print(stack.get_stack_top())
        elif condition == "Size":
            print(stack.get_size())
        elif condition == "Empty":
            print(stack.is_empty())
        elif condition == "Print":
            stack.print_stack()
        else:
            print("Invalid Condition!")
        text_in = input()
    stack.print_stack()

main()