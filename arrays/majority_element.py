#code
def majority_element():
    tc = int(input())
    test_data = []
    for c in range(tc):
        size = int(input())
        #n,d = list(map(int,input().split()))
        arr = list(map(int, input().split()))
        test_data.append(arr)

    for arr in test_data:
        half_size = len(arr) / 2

        dic = dict()
        major_element = -1
        for e in arr:
            if e in dic:
                dic[e] += 1
            else:
                dic[e] = 1
        for k, v in dic.items():
            if v > half_size:
                major_element = k
                break
        print(major_element)

if __name__ == '__main__':
    majority_element()
