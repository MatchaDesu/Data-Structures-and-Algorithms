class DataNode:

    def __init__(self, name=""):
        self.data = name
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self) :
        p = self.head

        if p == None :
            print("This is an empty list.")
            return

        while p :
            print(p.data, end=" -> "*(p.next != None))
            p = p.next
    
    def insert_last(self, data) :
        p = self.head
        self.count += 1

        if p == None :
            self.head = DataNode(data)
            return
        
        while p.next != None :
            p = p.next
        p.next = DataNode(data)
    
    def insert_front(self, data) :
        d = DataNode(data)
        d.next = self.head
        self.head = d
        self.count += 1

    def insert_before(self, node, data) :
        d = DataNode(data)
        s = self.head

        if s == None :
            print(f"Cannot insert,",node,"does not exist.")
            return

        if s.data == node :
            self.insert_front(data)
            return

        p = None

        while s != None and s.data != None :
            p = s
            s = s.next

            if s == None :
                print(f"Cannot insert,",node,"does not exist.")
                return
            
            if s.data == node :
                break

        p.next = d
        d.next = s
        self.count += 1

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #    mylist.delete(data)
        else:
            print("Invalid Condition!")
        mylist.traverse()
        print()

main()
