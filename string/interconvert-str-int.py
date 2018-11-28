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
print(strToInt("-123"))
print(strToInt("1234"))
