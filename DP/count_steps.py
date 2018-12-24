# this has 3^n time complexity
def count_steps_recursive(n):
    if n < 0:
        return 0
    elif n is 0:
        return 1
    else:
        return count_steps_recursive(n - 3) + count_steps_recursive(n - 2) + count_steps_recursive (n - 3)
def count_steps_dp(n, m):
    if n < 0:
        return 0
    elif n is 0:
        return 1
    elif m[n] != -1:
        return m[n]
    else:
        m[n] = count_steps_dp(n - 3, m) + count_steps_dp(n - 2, m) + count_steps_dp(n - 1, m)
        return m[n]



if __name__ == '__main__':
    #print(count_steps_recursive(50))
    n = 50
    m = [-1] * (n + 1)
    print(count_steps_dp(n , m))
