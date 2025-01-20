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

def main() :
    num = int(input())
    studentID = SinglyLinkedList()
    studentScore = SinglyLinkedList()
    total = 0

    for i in range(num) :
        number, score = input().split()
        studentID.insert_last(number)
        studentScore.insert_last(float(score))
        total += float(score)

    mean = total/num

    n = studentID.head
    s = studentScore.head
    topStudent = None
    highestScore = 0

    for _ in range(num) :

        if s.data > highestScore and s.data <= mean :
            topStudent = n.data
            highestScore = s.data

        n = n.next
        s = s.next

    print(topStudent,highestScore,sep="\t")
main()
