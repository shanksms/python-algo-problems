#code
def remove_dups():
    tc = int(input())
    for c in range(tc):
        size = int(input())
        #n,d = list(map(int,input().split()))
        arr = input().split()
        result_set = set()
        result = []
        for element in arr:
            if not element in result_set:
                result.append(element)
                result_set.add(element)


        print(' '.join(result))


if __name__ == '__main__':
    remove_dups()
