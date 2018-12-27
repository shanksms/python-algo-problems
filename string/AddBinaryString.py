def addBinaryString(s1, s2):
    n1 = convertToDecimal(s1)
    n2 = convertToDecimal(s2)

    n = n1 + n2
    return convertToBinary(n)


def convertToDecimal(s):
    n = 0
    for c in s:
        n = 2*n + int(c)
    return n
def convertToBinary(n):
    s = []
    while n > 0:
        s.append(str(n % 2))
        n //= 2
    s.reverse()
    return "".join(s)


if __name__ == '__main__':
    tc = int(input())
    for c in range(tc):
        s1, s2 = input().split()
        print(addBinaryString(s1, s2))
