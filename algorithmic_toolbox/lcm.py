# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
	result = 1
	if max(a,b) % min(a,b) != 0:
		return gcd(b%a, a%b)
	result = min(a, b)
	return result

def lcm(a, b):
	return int(a*b/gcd(a, b))


a, b = map(int, input().split())
print(lcm(a, b))

