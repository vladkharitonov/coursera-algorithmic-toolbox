# Uses python3
import sys
import math

def get_change(m):
	coins_10 = math.floor(m/10)
	m = m - coins_10 * 10
	coins_5 = math.floor(m/5)
	m = m - coins_5 * 5
	
	return int(m + coins_10 + coins_5)


m = int(input())
print(get_change(m))
