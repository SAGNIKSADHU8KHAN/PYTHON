class Parrot:

    species = "bird"

    def __init__(self,name,age):
    
       self.name = name
       self.age = age

koko = Parrot("koko", 10)
blue = Parrot("blue", 5)

print(" Blue is a {}".format(blue.species))
print(" Koko is also a {}".format(koko.species))


print(" {} is a beautiful bird.".format(blue.name))
print(" Blue is {} years old".format(blue.age))