#code
#code
tc = int(input())
nums = []
for i in range(tc):
    s1, s2 = input().split(' ')
    nums.append((int(s1), int(s2)))

for num in nums:
    rem = num[0] % num[1]
    first = num[0] - rem
    second = num[0] + (num[1] - rem)
    
    if abs(num[0] - first) is abs(num[0] - second):
        print(first if abs(first) > abs(second) else second)
    elif abs(num[0] - first) < abs(num[0] - second):
        print(first)
    else:
        print(second)
