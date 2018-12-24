def upsAndDowns():
    tc = int(input())
    test_data = []
    for c in range(tc):
        size = int(input())
        #n,d = list(map(int,input().split()))
        arr = list(map(int, input().split()))
        u = d = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                u += 1
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                d += 1

        print(u, end = ' ')
        print(d)
if __name__ == '__main__':
    upsAndDowns()
