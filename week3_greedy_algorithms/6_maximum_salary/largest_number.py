#Uses python3

import sys
from itertools import permutations
from numpy import random


def naive(a):
    res = ""
    output = ""
    for x in list(permutations(a, len(a))):
        if res <= output.join(x):
            res = output.join(x)
    return res

def largest_number(a):
    res = ""
    while len(a) > 0:
    	max_number = "0"
    	index = 0
    	for number in a:
    		max_number = compare(number, max_number)
    		index = a.index(max_number)
    	res += max_number
    	a.pop(index)
    return res

def compare(a, b):
    if int(a + b) >= int(b + a):
        return a
    else:
        return b

def stress():
    while True:
        a = [str(random.randint(0,1000)) for x in range(random.randint(1, 5))]
        print(a)
        largestResult = largest_number(a)
        naiveResult = naive(a)
        if largestResult == naiveResult:
            continue
        else:
            print("Wrong")
            print(a)
            break


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    
