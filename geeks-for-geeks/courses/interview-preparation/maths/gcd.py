def gcd(a, b):
    if a % b is 0:
        return b
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    print(gcd(20, 5))
