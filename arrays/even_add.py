def even_add(arr):
    #i indexes even, j indexes odd
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] % 2 == 0:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1



if __name__ == '__main__':
    a = [2, 2, 3, 4, 8, 6]
    even_add(a)
    print(a)
