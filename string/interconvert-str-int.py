def strToInt(s):
    num = 0
    isNeg = False
    if s.startswith('-'):
        s = s[1:]
        isNeg = True
    for c in s:
        #print(ord(c) - ord('0'))
        num = num * 10 + (ord(c) - ord('0'))
        #print(num)
    return -num if isNeg else num
def intToStr(num):
    strRepLs = []
    isNeg = False
    if num < 0:
        num, isNeg = -num, True
    while num > 0:
        strRepLs.append(chr(ord('0') +  num%10))
        num = num // 10

    return ('-' if isNeg else '') +  ''.join(reversed(strRepLs))


print(strToInt("-123"))
print(strToInt("1234"))
print(intToStr(12))
print(intToStr(-1234))
