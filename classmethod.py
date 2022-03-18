# making constructor
# __init__ is a constructor

class Seasia:
    leaves = 2

    def __init__(self , aname , acity): # this is consrtuctor
        self.name = aname
        self.city = acity
    
    def detail(self):
        return f"name is {self.name}. he is from {self.city}."
    
    @classmethod
    def new_leaves(cls , newleaves ):
        cls.leaves=newleaves


vikrant = Seasia( "vikrant" , "Hisar")
ajay = Seasia("ajay" , "Nepal")
 
#vikrant.name = "vikrant"
#vikrant.city = "hisar"

#ajay.name = "Ajay"
#ajay.city = "nepal"

vikrant.new_leaves(15)
#print(ajay.name)
#print(vikrant.detail())
 
print(vikrant.leaves)