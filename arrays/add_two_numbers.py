def add_two_arrays(A, B):
    if len(A) > len(B):
        B = [0] * (len(A) - len(B)) + B
    else:
        A = [0] * (len(B) - len(A)) + A
    #this will hold the result
    C = [0]*len(A)
    #carry
    c = 0

    for i in reversed(range(len(A))):
        sum = A[i] + B[i] + c
        c = 0
        if sum >= 10:
            C[i] = sum % 10
            c = sum // 10
        else:
            C[i] = sum
    if c is not 0:
        C = [c] + C
    return C

if __name__ == '__main__':
    print(add_two_arrays([9, 0, 0], [1, 0, 1]))
