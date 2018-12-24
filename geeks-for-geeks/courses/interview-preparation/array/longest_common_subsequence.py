def subsequence(arr, n):
    set_element = set(arr)
    sorted_arr = sorted(list(set_element))
    current_count, max_count = 1, 1
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] + 1 == sorted_arr[i + 1]:
            current_count += 1
            max_count = max_count if max_count > current_count else current_count
        else:
            current_count = 1
    return max_count

if __name__ == '__main__':
    print(subsequence([87, 56, 43, 91, 27, 65, 59, 36, 32, 51, 37, 28, 75,7,74, 76], 16))
