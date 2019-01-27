def searchFirstOccurrence(A, element):
    start, end, result = 0, len(A) - 1, -1

    while start <= end:
        mid = (start + end) // 2
        if A[mid] > element:
            end = mid - 1
        elif A[mid] == element:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result

if __name__ == '__main__':
    '''
    This is a variant of binary search
    here elements could duplicate. The task is to find out first element
    '''
    print(searchFirstOccurrence([1, 2, 2, 3, 4], 2))
    
