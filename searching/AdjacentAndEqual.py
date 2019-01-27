def adjAndEqual(A):

    i = 0
    count = 0
    while i < len(A) - 1:
        if A[i] == A[i + 1]:
            count += 1
            i += 2
        else:
            i += 1

    return count

if __name__ =='__main__':
    tc = int(input())
    for c in range(tc):
        size = int(input())
        A = list(map(int, input().split()))
        print(adjAndEqual(A))
