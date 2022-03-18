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


vikrant = Seasia( "vikrant" , "Hisar")
ajay = Seasia("ajay" , "Nepal")
kali = Seasia.string("Kali-firozpur")

print(kali.detail())
print(vikrant.static("ram"),"\n")

vikrant.static("ram")

