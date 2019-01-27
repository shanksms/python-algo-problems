def searchAnElementEqualToIndex(A):
    start, end = 0, len(A) - 1

    while  start <= end:
        mid = (start + end) // 2
        difference = A[mid] - mid
        if difference > 0:
            end = mid - 1
        elif difference == 0:
            return mid
        else:
            start = mid + 1

    return -1

if __name__ == '__main__':
    print(searchAnElementEqualToIndex([-2, 0, 2, 3, 6, 7, 9]))
