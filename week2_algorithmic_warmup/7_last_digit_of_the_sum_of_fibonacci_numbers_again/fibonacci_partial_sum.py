# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_partial_sum(n, m):
    f2 = [0,1,1]
    f5 = [0,1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1]
    first, second = f5[(n+1) % 20], f5[(m+2) % 20]

    if first%2==f2[(n+1)%3]:
        first = (first-1)%10 
    else:
        first = first+4

    if second%2==f2[(m+2)%3]:
        second = (second-1)%10 
    else:
        second = second+4

    if second < first:
        result = 10 + second - first
        return result
    else:
        return (second - first)

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
