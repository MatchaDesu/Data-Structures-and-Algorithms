class Student :
    def __init__ (self, name, gender, age, id, gpa) :
        self.name = name
        self.gender = gender
        self.age = age
        self.id = id
        self.gpa = gpa

    def getInfo(self) :
        return "Mr"*(self.gender == "Male")+"Miss"*(self.gender == "Female")+(f" {self.name} ({self.age}) ID: {self.id} GPA {self.gpa:.2f}")

p1 = Student(input(),input(),input(),input(),float(input()))
p2 = Student(input(),input(),input(),input(),float(input()))
p3 = Student(input(),input(),input(),input(),float(input()))

search = input()

for i in [p1,p2,p3] :
    if search == i.id :
        print(i.getInfo())
        break
else :
    print("Student not found")