#code
def swapBitsMethod1(x) :

    # Get all even bits of x
    even_bits = x & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bits = x & 0x55555555

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1

    # Combine even and odd bits
    return (even_bits | odd_bits)

def swapBitsMethod2(num):
    tmp = num
    i = 0
    while tmp:
        if ((num >> i) & 1) != ((num >> (i + 1)) & 1):
            num = num ^ (3 << i)
        i = i + 2
        tmp = tmp >> 2
    return num

if __name__ == '__main__':
    tc = int(input())
    nums = []
    for i in range(tc):
        nums.append(int(input()))

    for num in nums:
        print(swapBitsMethod2(num))
