
def lcs_using_dp(X, Y, m, n):
    result = 0
    K = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i is 0 or j is 0:
                K[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                K[i][j] = K[i - 1][j - 1] + 1
                result = max(result, K[i][j])
            else:
                K[i][j] = 0
    return result



if __name__ == '__main__':
    X = ['D', 'A', 'B', 'C']
    Y = ['D', 'A', 'B', 'C']
    m, n = len(X), len(Y)
    result = lcs_using_dp(X, Y, m, n)
    print(result)
