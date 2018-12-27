def primeNumbersUptoN(n):
    A = [True] * (n + 1)
    # starting index should be 2 as 2 is the first prime number
    s = 2

    while s * s <= n:
        if A[s] is True:
            # Set all those indices to False if they are divisible for s * (any integer)
            for i in range(s*s, n + 1, s):
                #print(i)
                A[i] = False
        s += 1

    primeList = [i for i, v in enumerate(A) if (i >= 2 and v is True)]
    return primeList
if __name__ == '__main__':
    print(primeNumbersUptoN(50))
