# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares(n):
    a = [0,1]
    for i in range(2, 60):
        a.append((a[i-1] + a[i-2])%10)
    return (a[n%60] * a[(n+1)%60]) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
