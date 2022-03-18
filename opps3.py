class Seasia:
    leaves = 2
    
    def detail(self):
        return f"name is {self.name}. he is from {self.city}."

vikrant = Seasia()
ajay = Seasia()
 
vikrant.name = "vikrant"
vikrant.city = "hisar"

ajay.name = "Ajay"
ajay.city = "nepal"

print(ajay.detail())