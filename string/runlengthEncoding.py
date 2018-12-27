def decode(s):
    r = []

    count = 0
    for c in s:
        if c.isdigit():
            count = 10*count + ord(c) - ord('0')
        else:
            r.extend([c] * count)
            count = 0
    return "".join(r)
def encode(s):
    r = []
    count = 1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            r.append( str(count) + s[i])
            count = 1
        else:
            count += 1

            #print(count)

    ##we need to append last character as well.
    ##above loop will not take in account of last character
    r.append( str(count) + s[len(s) - 1])
    return "".join(r)

if __name__ == '__main__':
    print(decode('2a10b'))
    print(encode('aabbbbbbbbbbc'))
