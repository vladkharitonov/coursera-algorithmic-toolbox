# Uses python3
import numpy as np

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
	a = [0,1]
	for i in range(2,n+1):
		a.append(a[i-1] + a[i-2])
	return a[n]

# def test():
# 	n = 0
# 	while (True):
# 		n = np.random.choice(10,1)
# 		if calc_fib(n) == calc_fib_fast(n):
# 			print("OK")
# 		else:
# 			print("Wrong")
# 			return n

# print(test())

n = int(input())
print(calc_fib_fast(n))