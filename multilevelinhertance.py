
class Phones:
    devices = ["calcutor", "tourch" ,"watch"] 

class P_gedget(Phones):
    devcies = ["calcutor" , "watch" , "laser light"]

class E_device(P_gedget):
    devices = ["Tv", "Washing Machine" , "Heater" "Calcuator"]

A = E_device()

print(A.devcies)