# making constructor
# __init__ is a constructor

class Seasia:
    no_of_leaves = 2

    def __init__(self , aname , acity): # this is consrtuctor
        self.name = aname
        self.city = acity
    
    def detail(self):
        return f"name is {self.name}. he is from {self.city}. he is geting {self.no_of_leaves}leaves in a month."
    
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

class Python:           
    no_of_leaves = 5

    def __init__(self , aname , acity , known): 
        self.name = aname
        self.city = acity
        self.own = known
    
    def bio(self):
        return f"My name is {self.name}.\nI am from {self.city}.\nI ahve been haired for DevOps traine, i know {self.own} languages." 

class DevOps(Python, Seasia):        # multiple Inheritence  must enter the series carefully due to constructor dependance.
    no_of_leaves = 6

    def __init__(self , aname , acity , known , modules): 
        self.name = aname
        self.city = acity
        self.own = known
        self.modules = modules
    
    def about(self):
        print("hello my name is", self.name , "I am from ", self.city )
 
vikrant = Seasia( "vikrant" , "Hisar")
ajay = Seasia("ajay" , "Nepal")
kali = Seasia.string("Kali-firozpur")

payal = Python("Payal", "Himachal", ["cpp", "c","html"])
pyush = Python("Pyush" , "jalander" , ["c","cpp", "HTML", "JAVA"])

harry = DevOps("Harry", "jahhar", ["cpp","c",".net","python"], ["Django", "cv2"] )

print(harry.about())
print(harry.no_of_leaves)    # for variable of class.
print(harry.detail())           # function of  another the class.


