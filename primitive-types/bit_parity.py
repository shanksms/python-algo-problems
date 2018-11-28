def count_bit_parity_brute_force(num):
    bit_parity = 0
    bit_count = 0
    while num:
        bit_count += num & 1
        num >>= 1
    return bit_count % 2

print(count_bit_parity_brute_force(3))
