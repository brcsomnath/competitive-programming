
seive = [1] * (10**7)

def build_seive(N):
    seive[0], seive[1] = 0, 0
    primes = []

    for i in range(2, N+1):
        if seive[i] == 1:
            for j in range(i*i, N+1, i):
                seive[j] = 0
            primes.append(i)
    return primes
