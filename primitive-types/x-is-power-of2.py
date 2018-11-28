def testOfPower2(x):
    if x & (x-1) == 0:
        return True
    else:
        return False

print(testOfPower2(63))
print(testOfPower2(64))
