#code
#code
tc = int(input())
nums = []
for i in range(tc):
    s1, s2, s3 = input().split(' ')
    nums.append((int(s1), int(s2), int(s3)))

for num in nums:
    x = num[0] ** num[1]
    k = num[2]
    result = 0
    while k > 0:
        result = x % 10
        x = x // 10
        k -= 1
    print(result)
