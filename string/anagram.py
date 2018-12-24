#code
tc = int(input())
lines = []
for i in range(tc):
    lines.append(input())

for line in lines:
    words = line.split(' ')
    if "".join(sorted(words[0])) == "".join(sorted(words[1])):
        print('YES')
    else:
        print('NO')
    
