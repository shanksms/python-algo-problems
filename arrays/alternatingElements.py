def alternatingElements():
    tc = int(input())
    for c in range(tc):
        s1, s2 = list(map(int, input().split()))
        #n,d = list(map(int,input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))

        i = 0
        result = []
        while i < s1 and i < s2:
            result.append(a1[i])
            result.append(a2[i])
            i += 1

        if i == s1 and s1 != s2:
            result.extend(a2[i:])
        elif i == s2 and s1 != s2:
            result.extend(a1[i:])
        result = list(map(str, result))
        print(" ".join(result))


if __name__ == '__main__':
    alternatingElements()
