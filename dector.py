
# dectors
# used for call a function  in another function.

def ram(shyam):
    def sita():
        print("sita start")
        shyam()
        print("sita stoped")
        print("\n\n")
    return sita

@ram
def laxman():
    print("I am laxman \n Ram mara bhia h sita mari bhabi h")

laxman()

@ram 
def hanuman():
    print("I am hanuman \n # Das")

hanuman()

