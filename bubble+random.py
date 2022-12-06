import random
import time


def main():
    
    X = []
    n = 10
    for j in range(n):
        X.append(random.randint(0, n))

    print(X)
    L = X

    #bubble sort
    start2 = time.time()
    count = 0
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j+1] < L[j]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
                count = count + 1
    stop2 = time.time()
    print(L)
    print("Time used for Bubble: " + str(stop2 - start2))
    print("Bubble Sort number of steps: " + str(count))


    #start with random sort
    start = time.time()
    count = 0
    while True:
        maxPos = len(X)-2
        randomPos = random.randint(0, maxPos)

        temp = X[randomPos]
        X[randomPos] = X[randomPos + 1]
        X[randomPos + 1] = temp
        count = count + 1

        isSorted = True
        for i in range(len(X)-1):
            if X[i] > X[i+1]:
                isSorted = False
        if isSorted:
            break
    stop = time.time()
    print("Time used for Random: " + str(stop - start))
    print("Random Sort number of steps: " + str(count))
    print(L)
            

if __name__ == "__main__":
    main()
