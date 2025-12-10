class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"My name is {self.name}.")
    
    def is_adult(self):
        if self.age >= 18:
            return True
        
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter M(Male), F(Female) or O(Others): ").upper()
    
s = Student(name, age, gender)

s.introduce()
print("Adult: ", s.is_adult())

        