def longestSubstring(s):
    result = []
    start = end = 0
    for i in range(len(s) - 1):
        if chr(ord(s[i]) + 1) == s[i+1]:
            end += 1
        elif s[i] == 'z' and s[i + 1] == 'a':
            end += 1
        else:
            result.append(s[start:end + 1])
            start = end = i + 1
    result.append(s[start:end + 1])
    return result
if __name__ == '__main__':
    tc = int(input())
    for c in range(tc):
        result = longestSubstring(input())
        maxLenString = ''
        for string in result:
            if len(string) > len(maxLenString):
                maxLenString = string

        print(maxLenString)
        print(len(maxLenString))
