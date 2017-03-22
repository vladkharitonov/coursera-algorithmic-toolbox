# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum(n):
    a = [0,1]
    for i in range(2,n+2):
        a.append((a[i-1] + a[i-2])%10)
    return a[n+1]-1



n = int(input())
print(fibonacci_sum(n))
