class Student:
    def __init__(self, naam, punten): # initialiseert de values van de student
        # Hier zit de controle over de input
        if not isinstance(punten, (int, float)) or punten < 0:
            raise ValueError(f"punten moet een getal van 0 of hoger zijn, kreeg: {punten!r}")
        self.naam = naam
        self.punten = punten

    def geslaagd(self):
        return self.punten >= 50

    def __str__(self): # geeft gewoon een string terug, print zelf niet
        status = "geslaagd" if self.geslaagd() else "niet geslaagd"
        return f"{self.naam}: {self.punten} punten ({status})"

    def toon(self):
        print(f"Student: {self.naam}")
        print(f"Punten:  {self.punten}")
        print("-" * 20)

    def verhoog_punten(self, extra):
        self.punten += extra


student1 = Student("Anna", 20)
# student2 = Student("Bram", 'veel')
student2 = Student("Bram", 70)

student2.verhoog_punten(10)

student1.toon()
student2.toon()

print(student1)
print(student2)
print(student1.geslaagd())

# De fout zit ingesloten in de klasse (incapsulation) 
# Lijn 4 -> Een dict kun je nergens afdwingen; een klasse is de plek waar afdwingen mogelijk wordt.
# Crash gebeurt bij het aanmaken - bijvoorbeeld 'veel' punten - en niet in één van de volgende functies
