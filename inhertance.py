# making constructor
# __init__ is a constructor

class Seasia:
    leaves = 2

    def __init__(self , aname , acity): # this is consrtuctor
        self.name = aname
        self.city = acity
    
    def detail(self):
        return f"name is {self.name}. he is from {self.city}. he is geting {self.leaves}leaves in a month."
    
    @classmethod
    def new_leaves(cls , newleaves ):
        cls.leaves=newleaves

    @classmethod
    def string(cls , string):
        #parms = string.split("-")
        #return cls(parms[0] , parms[1] )
        return cls(*string.split("-"))
    
    @staticmethod
    def static(word):
        print("Hello i am ", word)

class DevOps(Seasia):           # Single inhertance

    def __init__(self , aname , acity , known): 
        self.name = aname
        self.city = acity
        self.own = known
    
    def bio(self):
        return f"My name is {self.name}.\nI am from {self.city}.\nI ahve been haired for DevOps traine, i know {self.own} languages." 

vikrant = Seasia( "vikrant" , "Hisar")
ajay = Seasia("ajay" , "Nepal")
kali = Seasia.string("Kali-firozpur")

payal = DevOps("Payal", "Himachal", ["cpp", "c","html"])
pyush = DevOps("Pyush" , "jalander" , ["c","cpp", "HTML", "JAVA"])

print(payal.bio())
print(payal.detail())



