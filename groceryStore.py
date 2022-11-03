class GroceryStore:
    def __init__(self, pp, name, manager):
        self.proPrice = pp 
        self.name = name
        self.manager = manager

    def proAvailable(self):
        return list(self.proPrice.keys())

    def purchase(self, l):
        s = 0
        for i in l:
            s = s + self.proPrice.get(i)
        return s
    def speak(self):
        print("Hi! Welcome to " + self.name + "! I'm " + self.manager +
              "! Hope you enjoy your experience today!")

def main():
    catalog = {"hi-chews" : 3.99,
               "ice breakers" : 2.00,
               "kit-kat" : 1.50,
               "pen" : 1.99,
               "instant noodle" : 4.50,
               "haagan dazs" : 1.50,
               "lip balm" : 1.50,
               "starbucks" : 5.00,
               "aquafina" : 12.50,
               "lenyard" : 4.50,
               "mask" : 0.50}

    gg = GroceryStore(catalog, "Chiu's Gas Station", "Chiu")

    inventory = {"hi-chews" : 3,
               "ice breakers" : 3,
               "kit-kat" : 3,
               "pen" : 3,
               "instant noodle" : 3,
               "haagan dazs" : 3,
               "lip balm" : 3,
               "starbucks" : 3,
               "aquafina" : 3,
               "lenyard" : 3,
               "mask" : 3}
    

    while True:
        op = int(input("\nWhat would you like to do?\n1) Products Available \n2) Make Purchase\n3) Speak to manager\n4) Check Inventory\nEnter -1 if done\n"))
        if op == -1:
            break
        if op == 1:
            print(gg.proAvailable())
        if op == 2:
            toBuy = []
            while True:
                res = input("What would you like to buy? Enter STOP if done\n")
            
                if res == "STOP":
                    break
                else:
                    if inventory.get(res.lower()) < 1:
                        print("Sorry, we ran out of stock for those")
                    else:
                        temp = inventory.get(res.lower())
                        inventory.update({res.lower() : temp - 1})
                        toBuy.append(res.lower())
            
            
            print(toBuy)
            
            print("Total Amount: " + str(gg.purchase(toBuy)))
        if op == 3:
            gg.speak()
        if op == 4:
            print(inventory)
        


if __name__ == "__main__":
    main()
