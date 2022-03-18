from statistics import variance


class P3:
    public = "PUBLIC"               # public variable can be used any were
    _protacted = "PROCATED"             # protcted variable can be used by base class or drived class only. 
    __private =  "PRIVAT"               # private variable can't be print by any one. Need a sepical method to print. only used by the basse class. 

variable = P3()

print(variable.public)
print(variable._protacted)
# print(variable.__private)                           # doesent work beacuse this varialbe is private 
print(variable._P3__private)                        # this is way to print a private variable with class name then variable name.

