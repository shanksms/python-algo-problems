##This solution is wrong
## fix it
def longestDistinctChasrs(s):
    setOfChars = set()
    maxDistinctCount = currCount = 0
    for c in s:
        if c in setOfChars:
            maxDistinctCount = max(currCount, maxDistinctCount)
            setOfChars = set()
            setOfChars.add(c)
            currCount = 1
        else:
            currCount += 1
            setOfChars.add(c)
    return maxDistinctCount
if __name__ == '__main__':
    #aewergrththy
    tc = int(input())
    for c in range(tc):
        s = input()
        print(longestDistinctChasrs(s))
