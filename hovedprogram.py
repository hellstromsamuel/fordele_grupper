from student import Student
import random
import math

kjonn = ["mann", "kvinne"]
program = ["digøk", "prosa", "språk", "design"]
str_gruppe = 4

def lagTiStudenter():
    studenter = []
    for i in range(100):
        student = Student("Student"+str(i), random.choice(kjonn), random.choice(program))
        studenter.append(student)
    return studenter

def main():
    studenter = lagTiStudenter()
    studenter_gruppert = {}
    for student in studenter:
        s_kjonn = student.hentKjonn()
        if s_kjonn in studenter_gruppert:
            studenter_gruppert[s_kjonn].append(student)
        else:
            studenter_gruppert[s_kjonn] = [student]

    antall_grupper = math.ceil(len(studenter)/str_gruppe)
    grupper = [[] for _ in range(antall_grupper)]
    teller = 0
    for s_kjonn in studenter_gruppert:
        for student in studenter_gruppert[s_kjonn]:
            grupper[teller].append(student)
            teller += 1
            teller = teller if teller < antall_grupper else 0

    for i in range(len(grupper)):
        print("Gruppe " + str(i) +":")
        for student in grupper[i]:
            print(student)

if __name__ == "__main__":
    main()