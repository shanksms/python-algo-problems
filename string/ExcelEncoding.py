def convertHeaderToNumber(header):
    result = 0
    for c in header:
        result = 26 * result + (ord(c) - ord('A') + 1)

    return result

def convertNumberToHeader(headerNum):
    resultList = []
    while headerNum > 0:
        if headerNum % 26 == 0:
            resultList.append('Z')
            headerNum = headerNum//26 - 1
        else:
            resultList.append(chr(headerNum % 26 + ord('A') - 1))
            headerNum = headerNum // 26
    return "".join(reversed(resultList))

if __name__ == '__main__':
    print(convertHeaderToNumber('A'))
    print(convertHeaderToNumber('ZZ'))
    print(convertHeaderToNumber('ZA'))
    '''
    This program converts excel headers to a number.
    for example. A is 1, B is 2 ...Z is 26
    AA is 27 AB is 28 etc
    '''

    print(convertNumberToHeader(1))
    print(convertNumberToHeader(702))
    print(convertNumberToHeader(677))
