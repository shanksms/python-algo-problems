''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

 # Your task is to complete this function
# function should a list containing the required order of the elements
def threeWayPartition(arr, n, lowVal, highVal):
    A, B, C = [], [], []
    i = 0
    for c in range(i, len(arr)):
        e = arr[c]
        if e <= lowVal:
            A.append(arr[c])
            i += 1
        else:
            break
    for c in range(i, len(arr)):
        e = arr[c]
        if lowVal < e <= highVal:
            B.append(e)
            i += 1
        else:
            break
    for c in range(i, len(arr)):
        e = arr[c]
        if e > highVal:
            C.append(e)
            i += 1
        else:
            break
    if len(arr) == (len(A) + len(B) + len(C)):
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(threeWayPartition([1, 2, 3, 4, 5], 5, 1, 2))
