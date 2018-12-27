
def heavierString(s1, s2):
    sum1 = sum2 = 0
    for c in s1:
        sum1 = sum1 + ord(c)
    for c in s2:
        sum2 = sum2 + ord(c)

    if sum1 > sum2:
        return s1
    elif sum1 < sum2:
        return s2
    else:
        return 'equal'

if __name__ == '__main__':
    tc = int(input())
    for c in range(tc):
        print(heavierString(input(), input()))
