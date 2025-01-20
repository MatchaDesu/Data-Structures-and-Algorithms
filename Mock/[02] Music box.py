class Song :
    def __init__(self, name:str, genre:str, durations:int) :
        self.name = name
        self.genre = genre
        self.durations = int(durations)
        self.next = None
    
    def show_info(self) :
        minutes, seconds = divmod(self.durations, 60)
        return (f"{self.name} <|> {self.genre} <|> {minutes}.{seconds:>02}")

class ActionNode() :
    def __init__(self, action, durations, index, song):
        self.action = action
        self.durations = durations
        self.index = index
        self.song = song
        self.next = None
    
    def __str__ (self) :
        return "Action =",self.action,"\ndurations =",self.durations,"\nindex =",self.index,",\nsong = ",song.show_info()

class ActionStack() :
    def __init__(self) :
        self.top = None
    
    def push(self, action) :

        a = ActionNode(*action)

        if self.top == None :
            self.top = a
            return
        
        a.next = self.top
        self.top = a
    
    def pop(self) :
        if self.top == None :
            return

        pop_action = self.top
        self.top = pop_action.next
        pop_action.next = None

        return pop_action.action, pop_action.durations, pop_action.index, pop_action.song

class Queue:
    def __init__(self):
        self.action = ActionStack()
        self.total_time = 0
        self.head = None

    def enqueue(self, song: Song):
        
        if self.isEmpty() :
            self.head = song
            self.total_time += song.durations
            return
        
        p = self.head
        while p.next :
            p = p.next
        
        p.next = song

        self.total_time += song.durations
        self.action.push(("enqueue", song.durations, None, song))

    def dequeue(self):
        
        if self.isEmpty() :
            print("Underflow! Dequeue from an empty queue")
            return
        
        deq_song = self.head
        self.head = deq_song.next
        deq_song.next = None

        self.total_time -= deq_song.durations
        self.action.push(("dequeue", deq_song.durations, None, deq_song))
        return deq_song

    def peek(self):

        if self.isEmpty() :
            print("Underflow! peek from an empty queue")
            return
        return self.head

    def isEmpty(self):
        return not bool(self.head)

    def show_Queue(self):
        number = 0

        if self.isEmpty() :
            print("Queue is empty!")
            return

        currentNode = self.head

        while currentNode :
            number += 1
            print(f"Queue#{number}", currentNode.show_info())
            currentNode = currentNode.next
        
    def lastSong(self, time) :

        if self.isEmpty():
            print("There is no song in this queue!")
            return
        
        number = 0

        if time % self.total_time > 0 :
            time = time % self.total_time

        currentNode = self.head

        while currentNode :
            number += 1
            if time <= currentNode.durations :
                print(f"Queue#{number}", currentNode.show_info())
                break
            time -= currentNode.durations
            currentNode = currentNode.next

    def removeSong(self, name):
        index = 0
        currentNode = self.head
        prevNode = None

        if self.isEmpty() :
            print(f"Can not Delete! {name} is not exist")
            return
        
        if currentNode.name == name :
            self.dequeue()
            return

        while currentNode :

            if currentNode.name == name :

                prevNode.next = currentNode.next
                currentNode.next = None

                self.total_time -= currentNode.durations
                self.action.push(("remove", currentNode.durations, index, currentNode))

                return
            
            prevNode = currentNode
            currentNode = currentNode.next
            index += 1
                
        else :
            print(f"Can not Delete! {name} is not exist")

    def groupSong(self):
        if self.isEmpty() :
            print("Nothing here! Please add some song")
            return

        currentNode = self.head

        jpop = ""
        kpop = ""
        rb = ""

        while currentNode :
            match currentNode.genre :
                case "JPOP" :
                    jpop += f" {currentNode.name} |"
                case "KPOP" :
                    kpop += f" {currentNode.name} |"
                case "R&B" :
                    rb += f" {currentNode.name} |"

            currentNode = currentNode.next

        print("JPOP:"+jpop.rstrip(" |"))
        print("KPOP:"+kpop.rstrip(" |"))
        print("R&B:"+rb.rstrip(" |"))

    def undo(self):
        if self.action.top == None :
            return
        action, durations, index, song = self.action.pop()

        match action :
            case "enqueue" :
                currentNode = self.head
                prevNode = None

                while currentNode.next :
                    prevNode = currentNode
                    currentNode = currentNode.next
                
                if prevNode :
                    prevNode.next = None
                else :
                    self.head = None
                
                self.total_time -= durations
            
            case "dequeue" :
                song.next = self.head
                self.head = song
                self.total_time += durations
            
            case "remove" :
                if index == 0 :
                    song.next = self.head
                    self.head = song
                    self.total_time += durations
                    return

                currentNode = self.head
                prevNode = None

                for _ in range(index) :
                    if not currentNode.next :
                        currentNode.next = song
                        break
                    prevNode = currentNode
                    currentNode = currentNode.next

                else :
                    song.next = currentNode
                    prevNode.next = song
                
                self.total_time += durations
            
            case "reverse" :
                currentNode = self.head
                prevNode = None
                nextNode = None

                while currentNode :
                    nextNode = currentNode.next
                    currentNode.next = prevNode
                    prevNode = currentNode
                    currentNode = nextNode
                
                self.head = prevNode
            


    def rev_queue(self):
        
        currentNode = self.head
        prevNode = None
        nextNode = None

        while currentNode :
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        self.head = prevNode

        self.action.push(("reverse", None, None, None))

def main(): #อธิบายโค้ดในส่วนของ main()
    """this is main function"""
    q = Queue() #สร้าง Queue ว่างขึ้นมา
    while (choice := input()) != "End": #ลูปรับค่าไปเรื่อย ๆ จนกว่าจะเจอคำว่า End
        command, data = choice.split(": ") #แยก input ออกเป็น 2 ค่า คือ command ในการเรียกใช้แต่ละ methods และ data สำหรับใส่เป็น Arguments ของ methods นั้น ๆ ( ถ้ามี )
        match command: # ใช้ match-case เพื่อจับคู่คำสั่งการทำงาน
            case "enqueue":
                q.enqueue(Song(*data.split("|")))  # เพิ่ม object ที่สร้างจากคลาส Song เข้าไปที่ส่วนท้ายของคิว
            case "dequeue":
                temp = q.dequeue() # ทำการลบและคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp: # ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Dequeue item:", temp.show_info())
            case "peek":
                temp= q.peek() # ทำการคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp:# ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Peek item:", temp.show_info())
            case "isEmpty":  # เรียกใช้ isEmpty เพื่อดูว่าคิวว่างหรือไม่
                print(q.isEmpty())
            case "showQueue": # เรียกใช้ showQueue เพื่อแสดงผลข้อมูลเพลงในคิวตามลำดับ
                q.show_Queue()
            case "lastSong":  # เรียกใช้ lastSong เพื่อดูข้อมูลเพลงสุดท้ายที่จะได้ฟัง
                q.lastSong(int(data))
            case "removeSong": # เรียกใช้ removeSong เพื่อลบเพลงนั้นๆ ออกจากคิว
                q.removeSong(data)
            case "groupSong": # เรียกใช้ groupSong เพื่อแสดงชื่อเพลงตามประเภทของเพลง
                q.groupSong()
            case "undo": # เรียกใช้ undo เพื่อย้อนคืนการทำงาน
                q.undo()
            case "rev": # เรียกใช้ rev ย้อนกลับลำดับของเพลงในคิว
                q.rev_queue()
    q.show_Queue() # แสดงข้อมูลเพลงในคิว ก่อนจะจบการทำงานของฟังก์ชัน
main()