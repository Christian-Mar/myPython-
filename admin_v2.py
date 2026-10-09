class Student:
    def __init__(self, naam, punten): # initialiseert de values van de student
        # Hier zit de controle over de input
        self.naam = naam 
        self.punten = punten

    def toon(self):
        print(f"Student: {self.naam}")
        print(f"Punten:  {self.punten}")
        print("-" * 20)

    def verhoog_punten(self, extra):
        self.punten += extra


student1 = Student("Anna", 70)
# student2 = Student("Bram", 'veel')
student2 = Student("Bram", 30)

student2.verhoog_punten(10)

student1.toon()
student2.toon()

# De fout zit ingesloten in de klasse (incapsulation) 
# Bijvoorbeeld Student("Bram", "veel") -> student is corrupt, maar de rest van het programma blijft werken
