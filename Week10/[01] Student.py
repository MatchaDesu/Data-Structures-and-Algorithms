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

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())