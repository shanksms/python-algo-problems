#code
tc = int(input())
nums = []
for i in range(tc):
    nums.append(int(input()))

for num in nums:
    count = 0
    for i in range(1, num + 1):
        while i:
            count += 1
            i = i & (i - 1)
    print(count)
        
