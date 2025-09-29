def sieve_of_eratosthenes(n):

    prime = [True]* (n+1)

    prime[0], prime[1] = False, False

    p =2
    while p *p <= n:
        if prime[p]:

            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return prime

prime_flags = sieve_of_eratosthenes(99)

two_digit_primes = [i for i in range(10, 100) if prime_flags[i]]

print("Two digit prime numbers are  ")

print(two_digit_primes)