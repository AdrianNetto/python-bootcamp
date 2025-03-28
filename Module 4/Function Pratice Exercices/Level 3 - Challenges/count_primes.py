# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(n):
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, n+1, i):
                is_prime[multiple] = False
    return sum(is_prime)

print(count_primes(100))