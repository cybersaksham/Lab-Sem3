class Student:
    def __init__(self, name, age, tag):
        self.name = name
        self.age = age
        self.tag = tag

        if self.tag.lower() == "pg":
            print("Enter your cgpa: ", end="")
            self.cgpa = float(input())
            print("Enter your degree: ", end="")
            self.degree = input()
            print("Enter your journals: ", end="")
            self.journals = input()

    def getInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Tag: ", self.tag)

        if self.tag.lower() == "pg":
            print("CGPA: ", self.cgpa)
            print("Degree: ", self.degree)
            print("Journals: ", self.journals)


print("Enter UG student details: ")
nameUG = input("Name = ")
ageUG = int(input("Age = "))
ugStudent = Student(nameUG, ageUG, "UG")

print("Enter PG student details: ")
namePG = input("Name = ")
agePG = int(input("Age = "))
pgStudent = Student(namePG, agePG, "PG")

print()
print("UG Student Details:")
ugStudent.getInfo()
print()
print("PG Student Details:")
pgStudent.getInfo()
