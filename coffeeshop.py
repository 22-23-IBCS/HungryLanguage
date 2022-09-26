class CoffeeShop:
    def __init__(self):
        self.coffee = ""
        self.price = 0
        '''self.coffee = ""
         d = {"Coffee" : 4.00,
         "Latte": 3.50,
        "Hot Cider" : 4.50}
         self.coffee = 
         self.price = d["Iced coffee"]'''

    def setDrink(self, n):
        if n == 1:
            self.coffee = "Coffee"
        elif n == 2:
            self.coffee = "Latte"
        elif n == 3:
            self.coffee = "Hot cider"
        else:
            self.coffee = "Sorry. We don't have that here"

    def getDrink(self):
        if self.coffee == "Coffee":
            return "Coffee."
        elif self.coffee == "Latte":
            return "Latte."
        elif self.coffee == "Hot cider":
            return "Hot cider."

    def setPrice(self):
        if self.coffee == "Coffee":
            self.price=3.00
            
        elif self.coffee == "Latte":
            self.price=4.00
         
        elif self.coffee == "Hot cider":
            self.price=5.00
        else:
            return 0

    def getPrice(self):
        return self.price
    



def main():
    C = CoffeeShop()
    print("Hi, welcome to Junha's and Terence's Café. Please pick an option")
    
    myOrder=int(input("1. Coffee\n2. Latte\n3. Hot Cider\n"))
    C.setDrink(myOrder)
    C.setPrice()

    size = int(input("What size do you want? In ounces:\n"))

    print("Gotcha. "+"1 "+str(size)+ " oz "+C.getDrink())

    name = input("Can I get your name?\n")

    print("Got it. That will be $" + str(C.getPrice()) + " " + name + ".\n\nHere is your drink. Thanks!\nPlease come again")
    


if __name__ == "__main__":
    main()
