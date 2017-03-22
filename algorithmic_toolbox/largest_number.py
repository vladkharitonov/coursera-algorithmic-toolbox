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

def compare(a,b):
    if len(a) == len(b):
        return max(a, b)
    elif len(a) > len(b):
        for i in range(0, int(a)-int(b)):
            if a[i:(i+len(b))] == b:
                continue
            elif a[i:(i+len(b))] > b:
                return a
            else:
                return b
    else:
        for i in range(0, int(b)-int(a)):
            if b[i:(i+len(a))] == a:
                continue
            elif b[i:(i+len(a))] > a:
                return b
            else:
                return a

def stress():
    a = []
    while True:
        a = [str(random.randint(1,1000)) for x in range(5)]
        if largest_number(a) == naive(a):
            print(largest_number(a))
            print(naive(a))
            print("OK")
        else:
            print("Wrong")
            return a


# print(stress())
# print(naive(['23', '331', '507', '580', '315']))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    
