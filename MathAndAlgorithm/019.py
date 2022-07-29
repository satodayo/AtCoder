N = int(input())
A = list(map(int, input().split()))

red = 0
yellow = 0
blue = 0

for i in range(N):
    if A[i] == 1:
        red += 1
    elif A[i] == 2:
        yellow += 1
    elif A[i] == 3:
        blue += 1

R = (red * (red - 1) / 2) + (yellow * (yellow - 1) / 2) + (blue * (blue -1) / 2)

print(int(R))