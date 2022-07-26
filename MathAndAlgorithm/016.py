def GCD(A, B):
    while 1 <= A and 1 <= B:
        if A > B:
            A = A % B
        else:
            B = B % A
    if A >= 1:
        return A
    return B
    
N = int(input())
A = list(map(int, input().split()))

R = GCD(A[0], A[1])

for i in range(2, N):
    R = GCD(R, A[i])

print(R)