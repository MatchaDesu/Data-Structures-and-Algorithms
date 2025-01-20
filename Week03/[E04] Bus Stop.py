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
            print(p.data, end=" -> " if p.next != None else "\n")
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
    
    def enqueue(self) :
        p = self.head
        self.head = p.next
        p.next = None
        self.count -= 1
        return p.data
    
    def find_data(self, data) :
        p = self.head
        while p != None :
            if p.data == data :
                return True
            p = p.next
        return False

def insert_index(mainList, subList, index) :

    p = mainList.head
    for i in range(index) :
        p = p.next
    p.data = subList

def main() :
    maximum = int(input())
    total_sign = int(input())

    mainList = SinglyLinkedList()
    bus = SinglyLinkedList()

    current_station = 0
    dropped = 0

    for _ in range(total_sign) :
        mainList.insert_front(SinglyLinkedList())

    for i in range(total_sign) :
        can_go = SinglyLinkedList()
        for index, number in enumerate(map(int, input().split())) :
            if not index :
                current_station = number
                continue

            if number > current_station :
                can_go.insert_last(number)

        insert_index(mainList, can_go, current_station-1)

    station_pointer = mainList.head

    for i in range(1,total_sign+1) :
        #print(i, bus.count)

        while bus.find_data(i) :
            bus.delete(i)
            dropped += 1

        while bus.count < maximum and station_pointer.data.count > 0 :
            bus.insert_last(station_pointer.data.enqueue())

        station_pointer = station_pointer.next

        #bus.traverse()
    print(dropped)

main()
