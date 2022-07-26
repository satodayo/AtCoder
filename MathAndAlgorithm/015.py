def GCD(A, B):
    while 1 <= A and 1 <= B:
        if A > B:
            A = A % B
        else:
            B = B % A
    if A >= 1:
        return A
    return B
    
A, B = map(int, input().split())
print(GCD(A, B))