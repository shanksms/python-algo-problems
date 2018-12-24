#code
#code


def gcd(a, b):
    if a % b is 0:
        return b
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    tc = int(input())
    test_data = []
    for i in range(tc):
        size = int(input())
        arr = []
        arr_str = input().split(' ')
        for i in range(size):
            arr.append(int(arr_str[i]))
        test_data.append(arr)

    for ls in test_data:
        _gcd = ls[0]
        for i in range(1, len(ls)):
            _gcd = gcd(_gcd, ls[i])
        print(_gcd)
