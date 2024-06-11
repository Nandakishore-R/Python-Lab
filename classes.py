class Student:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name : {self.name}\nAge :  {self.age}"
    def disp(self):
        print("Name is ",self.name)
        print("Age is ",self.age)

    
class Teacher:
    name = ''
    
p1 = Student("Nandu",23)
print(p1)
p1.disp()
t = Teacher()
t.name = 'revathi'
print(t.name)