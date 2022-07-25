N = int(input())

result = []
limit = int(N ** 0.5)

for i in range(2, limit + 1):
    while N % i == 0:
        N /= i
        result.append(i)

if N > 2:
    result.append(int(N))

print(*result)