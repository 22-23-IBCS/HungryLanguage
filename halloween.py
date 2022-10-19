import random

class House:
    def __init__(self):
        self.rating = random.randint(1, 10)
        self.passed = False

    def shortestPath(self, n):
        return ""
    def getRating(self):
        return self.rating
    def passing(self):
        self.passed = True
    def getPass(self):
        return self.passed
        
def optimalChoice(n, x, y):
    nums = []
    
    if x <= 3 and not(n[x+1][y].getPass()):
        nums.append(n[x+1][y].getRating())
    else:
        nums.append(-1)
        
    if x >= 1 and not(n[x-1][y].getPass()):
        nums.append(n[x-1][y].getRating())
    else:
        nums.append(-1)
        
    if y <= 3 and not(n[x][y+1].getPass()):
        nums.append(n[x][y+1].getRating())
    else:
        nums.append(-1)
        
    if y >= 1 and not(n[x][y-1].getPass()):
        nums.append(n[x][y-1].getRating())
    else:
        nums.append(-1)

    m = max(nums)
    if m == -1:
        return [0, -1, -1]
    
    i = nums.index(m)
    if i == 0:
        return [m, x+1, y]
    elif i ==1:
        return [m, x-1, y]
    elif i ==2:
        return [m, x, y+1]
    elif i ==3:
        return [m, x, y-1]



def main():
    neighborhood = []
    originalSum = 0
    for i in range(5):
        housesTemp = []
        for j in range(5):
            housesTemp.append(House())
            originalSum = originalSum + housesTemp[j].getRating()
        neighborhood.append(housesTemp)

    print(neighborhood)
    
    x = int(input("Which house do you want to begin with? (Longitude)"))
    y = int(input("Which house do you want to begin with? (Latitude)"))
    n = int(input("How many houses do you want to visit?"))


    loc = [x, y]
    sums = 0
    neighborhood[loc[0]][loc[1]].passing()
    s  = int(neighborhood[loc[0]][loc[1]].getRating())
    sums = sums + s
    #print(s)
    
    for k in range (n-1):
        o = optimalChoice(neighborhood, loc[0], loc[1])
        sums = sums + int(o[0])
        #print(o[0])
        loc = [int(o[1]), int(o[2])]
        neighborhood[loc[0]][loc[1]].passing()
        
    
    print ("\nAverage of the " + str(n) + " houses visited:" + str(sums/n))

    print ("Average of all houses: " + str(originalSum/25))
        
        



if __name__ == "__main__":
    main()
