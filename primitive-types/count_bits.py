def count_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count

print(count_bits(3))
