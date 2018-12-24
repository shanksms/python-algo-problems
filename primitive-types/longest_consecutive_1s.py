#code
tc = int(input())
nums = []
for i in range(tc):
    nums.append(int(input()))

for num in nums:
    a = []
    count = 0
    while num:
        #print(num)
        c = num & 1
        num = num >> 1
        if c == 1:
            count += 1
        else:
            count = 0
        a.append(count)
    print(max(a))
