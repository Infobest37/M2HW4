numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

for k in numbers:
    is_prime = False
    if k > 1:
        for z in range(2, k):
            if k % z == 0:
                is_prime = True
                break
        if is_prime:
            not_primes.append(k)
print(f'primes =', primes)
print(f'not_primes =', not_primes)
