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
    f2 = [0,1,1]
    f5 = [0,1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1]
    y = f5[(n+2) % 20]
    if y%2==f2[(n+2)%3]:
        return (y-1)%10 
    else:
        return y+4


n = int(input())
print(fibonacci_sum(n))
