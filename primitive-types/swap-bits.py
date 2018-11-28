def swap_bits(num, i, j):
    #check if bits are different at both positions
    if (num >> i) & 1 != (num >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        num ^= bit_mask
    return num

print(swap_bits(8, 0, 3))
print(swap_bits(15, 0, 3))
print(swap_bits(16, 0, 4))
