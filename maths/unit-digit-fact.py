import math

def unit_digit():
    tc = int(input())
    test_data = []
    for i in range(tc):
        test_data.append(int(input()))

    for num in test_data:
        result_fact = math.factorial(num)
        print(result_fact % 10)


def fact(n):
    if n is 0 or n is 1:
        return 1
    else:
        return n * fact(n - 1)

if __name__ == '__main__':
    unit_digit()
