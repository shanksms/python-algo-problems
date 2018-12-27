def buildingWithMaxSunlight(a):

    count = 1
    maxHeightSeenSoFar = a[0]
    for i in range(1, len(a)):
        if a[i] > maxHeightSeenSoFar:
            count += 1
            maxHeightSeenSoFar = a[i]

    return count

if __name__ == '__main__':
    tc = int(input())
    for c in range(tc):
        size = int(input())
        print(buildingWithMaxSunlight((list((map(int, input().split()))))))
