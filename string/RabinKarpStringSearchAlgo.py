def rabinKarpStringSearch(s, t):
    #s is the substring to be searched in main string t
    base = 26
    thash = sHash = 0
    power = 1

    for i in range(len(s)):
        #power = power * base if i > 0 else 1
        if i > 0:
            power = power * base
        else:
            power = 1
        sHash = sHash * base + ord(s[i])
        thash = thash * base + ord(t[i])
    for i in range(len(s), len(t)):
        if (thash == sHash) and (t[i - len(s):i] == s):
            return (i - len(s))
        #Calculate the rolling hash
        thash = thash -  ord(t[i - len(s)]) * power
        thash = thash * base
        thash = thash + ord(t[i])

    if (thash == sHash) and (t[len(t) - len(s):] == s):
        return len(t) - len(s)
    return -1

if __name__ == '__main__':
    print(rabinKarpStringSearch('da', 'abcd'))
