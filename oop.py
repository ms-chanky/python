# object-oriented programming
# class Person:
#     def __init__(self):
#         self.name = "Naomi"
#         self.age = 17
#         self.gender ="Female"
#
#
# student = Person()
# student.name = "Kelly"
# print(student.name)
# print(student.age)

class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


person1 = People("Jane", 22, "female")
person2 = People("Judas", 34, "Male")
person3 = People("Peter", 29, "Male")
print(f"Hi. My name is {person1.name}.")


print(person1.name)
# print(person1.age, person1.gender)


