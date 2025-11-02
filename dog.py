class Dog:
    def __init__(self,name, agee):
        self.name = name
        self.agee= agee
    def barking(self):
        print(f"{self.name} is barking")

    def rename(self,new_name):
        self.name = new_name

    def birthday(self):
        self.agee += 1
        print(f"hbd {self.name} you are now {self.agee} years old")

dog1 = Dog('Abulahab', 5)
dog1.barking()
dog1.rename('Abujahel')
dog1.birthday()
class Calculator:
    def __init__(self,a,b ):
        self.a = a
        self.b =b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
number = Calculator(6,7)
print(number.add())
#real world calculator
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,value):
        self.result += value
    def subtract(self):
        self.result -= value
    def multiply(self):
        self.result *= value
    def divide(self):
        if value != 0:
            result /= value
        else:
            print("can not divided by zero")
    def clear(self):
        self.result = 0
    def show(self):
        print(f"Current result:{ self.result}")


