def missingAndRepeating():
    tc = int(input())
    for c in range(tc):
        n = int(input())
        #n,d = list(map(int,input().split()))
        arr = sorted(list(map(int, input().split())))
        d = dict()
        missing = dup = None
        for e in arr:
            if e in d:
                d[e] += 1
            else:
                d[e] = 1
        for i in range(1, n + 1):
            if i not in d:
                missing = i
            elif d[i] == 2:
                dup = i


        print(dup, end = ' ')
        print(missing)


if __name__ == '__main__':
    missingAndRepeating()
