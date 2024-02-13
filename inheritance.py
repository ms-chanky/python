class Animal:
    def animals(self):
        print("Can breath")

    def monkey(self):
        print("Can walk")

    def baboon(self):
        print("Can run")


# h = Animal()
# print(h.animals())

class Human(Animal):
    def mtu(self):
        print("Mtu lives on land")


being = Human()
print(being.mtu(), being.baboon(),  being.animals(), being.monkey())
