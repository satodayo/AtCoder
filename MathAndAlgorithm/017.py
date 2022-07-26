def GCD(A, B):
    while 1 <= A and 1 <= B:
        if A > B:
            A = A % B
        else:
            B = B % A
    if A >= 1:
        return A
    return B

# A = Ga, B = Gb (a,bは互いに素、Gは最大公約数)
# L = Gab
#   = Ab
#   = A(B/G)
#   = AB/G
# 相手が持ってて自分に足りてないものをかけ合わせるイメージ
def LCM(A, B):
    return int(A / GCD(A,B))* B


N = int(input())
A = list(map(int, input().split()))

R = LCM(A[0], A[1])

for i in range(2, N):
    R = LCM(R, A[i])

print(R)