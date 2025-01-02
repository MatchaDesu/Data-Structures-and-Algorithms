
name = []
gender = []
age = []
id = []
gpa = []

for i in range(3) :
    name.append(str(input()))
    gender.append(str(input()))
    age.append(str(input()))
    id.append(str(input()))
    gpa.append(float(input()))

try :
    index = id.index(str(input()))
    print("Mr"*(gender[index] == "Male")+"Miss"*(gender[index] == "Female"),end=" ")
    print(f"{name[index]} ({age[index]}) ID: {id[index]} GPA {gpa[index]:.2f}")
except :
    print("Student not found")
