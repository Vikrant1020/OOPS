
class Seasia:
    leaves = 2

    def __init__(self , aname , acity, salary): # this is consrtuctor
        self.name = aname
        self.city = acity
        self.salary = salary
    
    def details(self):
        return f"hello {self.name}, are you from {self.city}. we can only give you {self.salary}"

    def __add__(self, other):                       # opertare overloading
        return self.salary + other.salary
    
    def __repr__(self):
        return f"Employe details are (name :{self.name}, from :{self.city}, salary given:{self.salary})"

amit = Seasia("Amit kumar", "Hisar" , 10000)
vivek = Seasia("Vivek kumar", "Ambala", 11000)

print(amit + vivek)
print(amit)