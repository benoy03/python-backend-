

def primes():
    yield 2
    found = [2]
    n = 3
    while True:
        is_prime = True
        limit = int(n ** 0.5)
        for p in found:
            if p > limit:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            found.append(n)
            yield n
        n += 2



prime_gen = primes()
for _ in range(6):
    print(next(prime_gen), end=" ")

