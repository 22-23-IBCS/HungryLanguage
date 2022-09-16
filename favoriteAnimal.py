
class Dog:

    def __init__(self, b, a, o, i):
        self.breed = b
        self.age = a
        self.owner = o
        self.intimacy = i
        print(self.owner + "'s " + self.breed + " is " + str(self.age) + " years old")

    def getIntimacy(self):
        return self.intimacy
    def increaseIntimacy(self, n):
        self.intimacy += n
    def getAge(self):
        return self.age

    def returnIntimacy(self):
        if (self.intimacy < 5):
            return ("The " + self.breed + " has just known his owner")
        else:
            return ("The " + self.breed + " has a great relationship with his owner")
        return ""
    def setIntimacy(self, n):
        self.intimacy = n

    def getIntimacy(self):
        return self.intimacy

def main():
    dog1 = Dog("Corgi", 1, "Terry", 4)
    dog2 = Dog("Samoyed", 5, "Mark", 8)

    
    print("How intimate are the dogs and their owners?")
    print(dog1.returnIntimacy())
    print(dog2.returnIntimacy())
    print("\n")

    dog1.setIntimacy(9)
    print(dog1.returnIntimacy())
    

    


if __name__ == "__main__":
    main()
