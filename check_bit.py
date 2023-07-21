def check_bit_set(A, B):
    mask = 1 << B
    if A & mask != 0:
        return 1
    else:
        return 0
A = int(input())
B = int(input())
print(check_bit_set(A, B))
