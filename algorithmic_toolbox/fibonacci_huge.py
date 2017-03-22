# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     unique = set(factors)
#     for i in range(0,len(unique)):

#     print len(unique)
#     return factors


def get_fibonacci_huge(n, m):
    a = [0,1]
    b = 1
    for i in range(2,n+1):
        a.append((a[i-1] + a[i-2])%m)
        if a[i-1] == 0 and a[i] == 1:
            b = len(a)-3
            return a[n%b-1]

    return a[n-1]%m



n, m = map(int, input().split())
print(get_fibonacci_huge(n, m))
