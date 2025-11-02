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

