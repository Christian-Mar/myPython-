def maak_student(naam, punten): # parameters meegeven met de functie
    return {"naam": naam, "punten": punten} # in dict zetten 


def toon_student(student):
    print(f"Student: {student['naam']}") # 'naam' is de key
    print(f"Punten:  {student['punten']}") # 'punten' is de key
    print("-" * 20)


def verhoog_punten(student, extra):
    student["punten"] += extra


student1 = maak_student("Anna", 10) # student in variabele steken
# student2 = maak_student("Bram", 'veel')
student2 = maak_student("Bram", 20)

verhoog_punten(student2, 10) # student bewerken met functie

toon_student(student1) # student ophalen 
toon_student(student2)

# Foutbron ligt bij de gebruiker: neemt hij de verkeerde dict en de functie kan er niets mee doen dan crasht het.