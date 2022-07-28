N = int(input())
A = list(map(int, input().split()))

one = 0
two = 0
three = 0
four = 0

for i in range(N):
    if A[i] == 100:
        one += 1
    elif A[i] == 200:
        two += 1
    elif A[i] == 300:
        three += 1
    elif A[i] == 400:
        four += 1
R = (one * four) + (two * three)

print(R)