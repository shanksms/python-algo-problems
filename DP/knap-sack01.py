
def knapsack(total_weight, w, val, n):
    k = [[0 for i in range(total_weight + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(total_weight + 1):
            if i is 0 or j is 0:
                k[i][j] = 0
            elif w[i - 1] > j:
                k[i][j] = k[i - 1][j]
            else:
                k[i][j] = max(val[i - 1] + k[i - 1][j - w[i - 1]], k[i - 1][j])


    return k[n][total_weight]
if __name__ == '__main__':
    w = [1, 4, 3]
    value = [1500, 3000, 2000]
    n = len(w)
    total_weight = 4
    print(knapsack(total_weight, w, value, n))
