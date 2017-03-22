# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
	result = 1
	if max(a,b) % min(a,b) != 0:
		return gcd(b%a, a%b)
	result = min(a, b)
	return result

a, b = map(int, input().split())
print(gcd(a, b))
