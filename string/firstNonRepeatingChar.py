def firstNonRepeatingChar(s):

    count = 1
    foundChar = None
    visited = set()
    for c in s:
        if (not c in s[count:]) and (not c in visited):
            foundChar = c
        else:
            count += 1
            visited.add(c)
    if foundChar is None:
        return -1
    else:
        return foundChar
if __name__ == '__main__':
    tc = int(input())
    for c in range(tc):
        count = int(input())
        print(firstNonRepeatingChar(input()))
