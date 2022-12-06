import random
import time


def main():

    X = []
    n = 20
    for k in range(n):
        X.append(random.randint(0, n))
    print(X)

    start = time.time()
    for i in range(n-1):
        minnum = i
        for j in range(i, n):
            if X[j]< X[minnum]:
                minnum = j
        temp = X[i]
        X[i] = X[minnum]
        X[minnum] = temp

    stop = time.time()

    print("Time spent: " + str(stop - start))
    print(X)

if __name__ == "__main__":
    main()
