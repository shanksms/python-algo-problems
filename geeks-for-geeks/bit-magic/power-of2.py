#code
tc = int(input())
nums = []
for i in range(tc):
    nums.append(int(input()))

for num in nums:
    if num and (num & (num -1)) is 0:
        print('YES')
    else:
        print('NO')
