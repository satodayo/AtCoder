N = int(input())

result = []
limit = int(N ** 0.5)

for i in range(1, limit + 1):
    if N % i == 0:
        result.append(i)
        if(i != N/i):
            result.append(int(N/i))

print(*result)