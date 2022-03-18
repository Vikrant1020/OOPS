class A:
    var1 = "it is a class A variable"
    def __init__(self):
        self.var1="this variable is in init of class A"
        self.vara = "this a variable in class A"
    
class B(A):
    var2 = "It is a variable in class B"
    def __init__(self):
        self.var1= "this a variable in class B"                 # over riding line 2.
        self.vara = "this  is a variable in class B"            # over riding second variable in constructor of class A.

a=A()
b=B()

print(b.vara)
print(b.var2)

