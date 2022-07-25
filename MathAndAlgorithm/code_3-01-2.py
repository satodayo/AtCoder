def isprime(N):
    limit = int(N ** 0.5)

    for i in range (2, limit + 1):
        if N % i == 0:
            return False
    return True

N = int(input())
bPrime = isprime(N)
if(bPrime):
    print("Yes")
else:
    print("No")