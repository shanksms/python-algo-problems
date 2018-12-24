#code
tc = int(input())
nums = []
for i in range(tc):
    nums.append(int(input()))

for num in nums:
    count = 0
    while num:
        count += 1
        num = num & (num-1)
    print(count)
