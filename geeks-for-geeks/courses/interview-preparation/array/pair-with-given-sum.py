#code
def pair():
    tc = int(input())
    test_data = []
    for c in range(tc):
        size = int(input())
        #n,d = list(map(int,input().split()))
        arr = list(map(int, input().split()))
        desired_sum = int(input())
        test_data.append((arr, desired_sum))

    for tup in test_data:
        arr, desired_sum = tup
        i, j = 0, len(arr) - 1
        sumfound = False
        while i < j:
            if (arr[i] + arr[j]) == desired_sum:
                print(arr[i], end = ' ')
                print(arr[j], end = ' ')
                print(desired_sum)
                sumfound = True
                i += 1
                j -= 1
            elif (arr[i] + arr[j]) > desired_sum:
                j -= 1
            else:
                i += 1
        if not sumfound:
            print(-1)

if __name__ == '__main__':
    pair()
