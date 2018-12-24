# this solution is not working
def the_great_one():
    tc = int(input())
    test_data = []
    for i in range(tc):
        size = int(input())
        int_arr = [int(float(i)) for i in input().split(' ')]
        test_data.append(int_arr)

    for int_arr in test_data:
        tup_arr = []
        count = 0
        set_of_nums = set()
        for el1 in int_arr:
            for el2 in int_arr:
                if el1 % el2 is 0:
                    count += 1
            tup_arr.append((el1, count))
            count = 0
        for tup in tup_arr:
            i, j = tup
            if j is 3:
                set_of_nums.add(i)
        set_of_nums = sorted(set_of_nums, reverse=True)
        result = 0

        for element in set_of_nums:
            result = result * 10 + element
        if result is 0:
            print(-1)
        else:
            print(result)
if __name__ == '__main__':
    the_great_one()
