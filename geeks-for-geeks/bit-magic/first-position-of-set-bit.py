#code
#code
tc = int(input())
nums = []
for i in range(tc):
    nums.append(int(input()))

for num in nums:
    count = 1
    if num & (num - 1):
        print(-1)
    else:
        while num:
            result = num  & 1
            if result is 1:
                break
            else:
                count += 1
                num = num >> 1

        print(count)
