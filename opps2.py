class Helo:
    am ="vikrant"
    pass

vikrant = Helo()
ankur = Helo()

vikrant.clas = "bsc CA"
vikrant.subject = ["phy","chem","computer"]

ankur.clas = "bsc cs"
ankur.subject = ["maths","comp","bio"]

print(vikrant.am , ankur.am)
print(ankur.subject, vikrant.subject)
print(Helo.__dict__)
