import json
class Student :

    def __init__(self, std_id : int, name : str, gpa : float) :
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self) -> int :
        return self.__std_id

    def get_name(self) -> str :
        return self.__name

    def get_gpa(self) -> float :
        return self.__gpa
    
    def print_details(self) -> None :
        print(f"ID: {self.get_std_id()}",f"Name: {self.get_name()}",f"GPA: {self.get_gpa():.2f}",sep="\n")

def binarySearch(data : list, name : str) :
    begin = 0
    end = len(data) - 1
    compare_time = 0
    
    while begin <= end :
        compare_time += 1
        mid = (begin + end) // 2
        if name > data[mid].get_name() :
            begin = mid + 1
        elif name < data[mid].get_name() :
            end = mid - 1
        else :
            begin = end + 1
    
    if (name == data[mid].get_name()) :
        print(f"Found {name} at index {mid}")
        data[mid].print_details()
    else :
        print(f"{name} does not exists.")
    
    print(f"Comparisons times: {compare_time}")

def main():
    import json
    data = []
    std = json.loads(input())

    for i in std :
        std = Student(i["id"], i["name"], i["gpa"])
        data.append(std)
    
    binarySearch(data,input())

main()
