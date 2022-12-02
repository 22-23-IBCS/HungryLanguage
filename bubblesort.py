import random

def main():
    L = [1,9,3,4,7,2,13,5,10,2]
    count = 0
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j+1] < L[j]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
                count = count + 1

    print(L)
    L = [1,9,3,4,7,2,13,5,10,2]
    #random sort
    while True:
        maxPos = len(L)-2
        randomPos = random.randint(0, maxPos)

        temp = L[randomPos]
        L[randomPos] = L[randomPos + 1]
        L[randomPos + 1] = temp

        isSorted = True
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                isSorted = False
        if isSorted:
            break
    print(L)
            

if __name__ == "__main__":
    main()
