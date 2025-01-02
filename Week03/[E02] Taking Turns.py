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
    
    def delete(self, data) :
        s = self.head

        if s == None :
            print(f"Cannot delete,",data,"does not exist.")
            return

        if s.data == data :
            self.head = s.next
            s.next = None
            self.count -= 1
            return

        p = None

        while s != None and s.data != None :
            p = s
            s = s.next

            if s == None :
                print(f"Cannot delete,",data,"does not exist.")
                return
            
            if s.data == data :
                break
        
        p.next = s.next
        s.next = None
        self.count -= 1
    
    def delete_last(self) :
        s = self.head
        for _ in range(self.count - 2) :
            s = s.next
        
        s.next = None
        self.count -= 1

    def delete_front(self) :
        s = self.head
        self.head = s.next
        self.count -= 1
    
    def getLast(self) :
        s = self.head
        if self == None :
            return None
        
        while s.next != None :
            s = s.next
        return s.data
        
    def getFront(self) :
        if self.head == None :
            return None
        return self.head.data

def main() :

    myList = SinglyLinkedList()
    newOrderList = SinglyLinkedList()
    forward = False
    left = 0
    right = 0

    num = int(input())

    for i in range(num) :
        myList.insert_last((input()))
    
    while myList.count > 0 :

        if forward :
            newOrderList.insert_last(myList.getFront())
            myList.delete_front()
            left += 1

        else :
            newOrderList.insert_last(myList.getLast())
            myList.delete_last()
            right += 1

        if left != right :
            forward = not forward
    newOrderList.traverse()
main()