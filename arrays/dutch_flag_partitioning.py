def dutch_flag_partitioning(pivot_index, elements):
    pivot = elements[pivot_index]
    smaller, equal, larger = 0, 0, len(elements)-1

    while equal < larger:
        if elements[equal] < pivot:
            smaller, equal = smaller + 1, equal + 1
            elements[smaller], elements[equal] = elements[equal], elements[smaller]
        elif elements[equal] == pivot:
            equal += 1
        else:
            elements[equal], elements[larger] = elements[larger], elements[equal]
            larger -= 1
    return elements
if __name__ == '__main__':
    print(dutch_flag_partitioning(2, [1, 0, 0, 2, 0, 3]))
