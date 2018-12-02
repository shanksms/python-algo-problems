def plus_some_number(elements, toAdd):
    #to carry
    c = 0


    for i in reversed(range(len(elements))):
        #e is the result of addition of digit at ith indexe

        e = elements[i] + c + toAdd
        #d should be added to only digit at last index
        toAdd = 0
        #re initialize c
        c = 0

        if e >= 10:
            c = e // 10
            elements[i] = e % 10
        else:
            elements[i] = e
    if c != 0:
        #we need to account carry which was supposed to be for 1st digit
        elements = [c] + elements

    return elements
def plus_one(elements):
    elements[-1] += 1
    for i in reversed(range(1, len(elements))):
        if elements[i] != 10:
            break
        else:
            elements[i] = 0
            elements[i - 1] += 1

    if elements[0] is 10:
        elements[0] = 1
        elements.append(0)
    return elements

if __name__ == '__main__':
    #print(plus_some_number([9, 9, 5], 5))
    print(plus_one([9, 9, 9]))
