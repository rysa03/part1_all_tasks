class Person:

    def __init__(self,name):
        self.name = name

    
    def speak(self):
        pass


class Dungan(Person):
    def speak(self):
        print("Hod' ni matsam genii")

class Uygur(Person):
    def speak(self):
        print("Man yugurcha daime")

class Osoba(Dungan, Uygur):
    def __init__(self, avto):
        Dungan.__init__(self, name)
        self.avto = auto


    def speak(self):
        print("Ya chototo govoryu")


Rahim = Osoba("Rahim", "AUDI")
Bekhzod = Uygur("Bekhzod")
Abdulkaarim = Dungan("Abdulkaarim")

for person in (Rahim, Bekhzod, Abdulkaarim):
    person.speak()

    