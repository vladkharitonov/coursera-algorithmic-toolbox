# Uses python3
import random
import numpy


n = int(input())
a = [int(x) for x in input().split(' ')]
assert(len(a) == n)


# def slow_solution(n, a):
# 	result = 0
# 	for i in range(0, n):
# 		for j in range(i+1, n):
# 			if a[i]*a[j] > result:
# 				result = a[i]*a[j]
# 	return result


def fast_solution(n, a):
	first_big = 0
	sec_big = 0
	for i in range(0, n):
		if a[i] >= first_big:
			sec_big = first_big
			first_big = a[i]
		if a[i] < first_big and a[i] > sec_big:
			sec_big = a[i]
	return first_big * sec_big


# def test():
# 	n = 0
# 	a = []
# 	while (True):
# 		n = int(numpy.random.choice(20,1) + 1)
# 		a = numpy.random.choice(10,n)
# 		if slow_solution(n, a) == fast_solution(n, a):
# 			print ("OK")
# 		else:
# 			print (a)
# 			print (slow_solution(n, a) + " " + fast_solution(n, a))
# 			return ("Wrong Answers")

print(fast_solution(n, a))