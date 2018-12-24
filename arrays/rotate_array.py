#code
t = int(input())
for c in range(t):
    n,d = list(map(int,input().split()))
    arr = input().split()
    result = []
    result.extend(arr[d:n])
    result.extend(arr[0:d])
    print(' '.join(result))
