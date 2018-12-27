def missingNumberInArray(A):
    n = len(A)
    sumOfNNumbers = ((n + 1) * (n + 2)) // 2
    sumOfArrayElements = 0

    for c in A:
        sumOfArrayElements = sumOfArrayElements + c

    return (sumOfNNumbers - sumOfArrayElements)

if __name__ == '__main__':
    tc = int(input())
    for c in range(tc):
        size = int(input())
        print(missingNumberInArray((list((map(int, input().split()))))))
