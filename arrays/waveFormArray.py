def waveFormArrayMethod1(elements):
    #sort the array
    elements = sorted(elements)
    print(elements)
    #swap even and odd positions values
    i = 0
    while i < (len(elements) - 1):
        elements[i], elements[i + 1] =  elements[i + 1], elements[i]
        i += 2
    return elements

def waveFormArrayMethod2(elements):
    for i in range(len(elements)):
        elements[i: i + 2] = sorted(elements[i: i + 2], reverse=i % 2)
    return elements

if __name__ == '__main__':
    print(waveFormArrayMethod2([6, 5, 4, 3, 2, 1]))
