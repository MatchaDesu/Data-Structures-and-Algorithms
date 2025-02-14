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

class ProbHash :

    def __init__(self, size : int) :
        self.__hash_table = [None] * size
        self.__size = size
    
    def hash(self, key : int) -> int :
        return key % self.__size
    
    def rehash(self, hkey : int) -> int :
        return (hkey + 1) % self.__size

    def insert_data(self, student : Student) -> None :
        hash_result = self.hash(student.get_std_id())

        while self.__hash_table[hash_result] :
            hash_result = self.rehash(hash_result)

            if hash_result == self.hash(student.get_std_id()) :
                print(f"The list is full. {student.get_std_id()} could not be inserted.")
                return

        self.__hash_table[hash_result] = student
        print(f"Insert {student.get_std_id()} at index {hash_result}")

    def search_data(self, std_id : int) -> Student :
        hash_result = self.hash(std_id)

        while self.__hash_table[hash_result] :
            if self.__hash_table[hash_result].get_std_id() != std_id :
                hash_result = self.rehash(hash_result)
            else :
                break

            if hash_result == self.hash(std_id) :
                print(f"{std_id} does not exits.")
                return
        else :
            print(f"{std_id} does not exist.")
            return

        print(f"Found {std_id} at index {hash_result}")
        return self.__hash_table[hash_result]

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
